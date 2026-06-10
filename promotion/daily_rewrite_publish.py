#!/usr/bin/env python3
import argparse, base64, datetime as dt, html, json, os, re, shutil, subprocess, sys, textwrap, time
from pathlib import Path

import requests
from requests_oauthlib import OAuth1

ROOT = Path('/root/.openclaw/workspace')
REPO = ROOT / 'claude-code-guide'
TOOLS = (ROOT / 'TOOLS.md').read_text(errors='ignore')
STATE = REPO / 'promotion/daily_series/state.json'
OUTDIR = REPO / 'promotion/daily_series/generated'
RESULTS = REPO / 'promotion/daily_series/results.jsonl'
OUTDIR.mkdir(parents=True, exist_ok=True)
RESULTS.parent.mkdir(parents=True, exist_ok=True)

CAMPAIGN = 'claude_code_guide_daily'
GITHUB_REPO_URL = 'https://github.com/xujfcn/claude-code-guide'
CRAZYROUTER_API = 'https://crazyrouter.com/v1/chat/completions'
MODEL = os.environ.get('CRAZYROUTER_REWRITE_MODEL', 'gpt-5.5')


def section(name: str) -> str:
    idx = TOOLS.find('## ' + name)
    if idx < 0:
        return ''
    nxt = TOOLS.find('\n## ', idx + 1)
    return TOOLS[idx:nxt if nxt != -1 else len(TOOLS)]


def val(block: str, key: str):
    m = re.search(r'- \*\*' + re.escape(key) + r'\*\*:\s*(.+)', block)
    return m.group(1).strip() if m else None


def find_crazyrouter_key() -> str:
    # Prefer explicit OpenAI-compatible Bearer from TOOLS examples.
    patterns = [
        r'Authorization: Bearer\s+([A-Za-z0-9_\-\.]+)',
        r'Bearer\s+(sk-[A-Za-z0-9_\-]+)',
        r'API Key\*\*:\s*(sk-[A-Za-z0-9_\-]+)',
    ]
    for pat in patterns:
        m = re.search(pat, TOOLS)
        if m:
            return m.group(1).strip()
    raise RuntimeError('Crazyrouter API key not found in TOOLS.md')


def github_push(repo: Path, message: str, paths=None):
    subprocess.run(['git', '-C', str(repo), 'add'] + (paths or ['.']), check=True)
    st = subprocess.run(['git', '-C', str(repo), 'diff', '--cached', '--quiet'])
    if st.returncode == 0:
        return 'nothing to commit'
    subprocess.run(['git', '-C', str(repo), 'commit', '-m', message], check=True)
    text = TOOLS
    m = re.search(r'Personal Access Token\*\*: (ghp_[A-Za-z0-9_]+)', text)
    if not m:
        raise RuntimeError('GitHub token not found')
    token = m.group(1).strip()
    header = base64.b64encode(f'x-access-token:{token}'.encode()).decode()
    proc = subprocess.run(
        ['git', '-C', str(repo), '-c', f'http.https://github.com/.extraheader=AUTHORIZATION: basic {header}', 'push', 'origin', 'main'],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if proc.returncode:
        raise RuntimeError((proc.stdout + proc.stderr).replace(token, '***'))
    return (proc.stdout + proc.stderr).replace(token, '***').strip()


def source_articles():
    return sorted((REPO / 'articles').glob('*.md'))


def source_title(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return fallback


def slugify(s: str, max_len=72) -> str:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return (s[:max_len].strip('-') or 'claude-code-guide')


def call_llm(prompt: str) -> str:
    key = find_crazyrouter_key()
    payload = {
        'model': MODEL,
        'messages': [
            {'role': 'system', 'content': 'You are a senior developer-marketer. Rewrite source tutorials into original, useful platform-ready technical articles. Avoid hype. Keep API endpoints clean; UTM only on human links.'},
            {'role': 'user', 'content': prompt},
        ],
        'temperature': 0.4,
        'max_completion_tokens': 5000,
    }
    r = requests.post(CRAZYROUTER_API, headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}, json=payload, timeout=300)
    if not r.ok:
        # Fallback for models that reject max_completion_tokens
        payload.pop('max_completion_tokens', None)
        payload['max_tokens'] = 5000
        r = requests.post(CRAZYROUTER_API, headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}, json=payload, timeout=300)
    r.raise_for_status()
    return r.json()['choices'][0]['message']['content'].strip()


def make_prompt(src_path: Path, src_md: str, idx: int):
    return f"""
Rewrite this Claude Code Chinese source article into a daily multi-platform publishing package.

Source index: {idx}
Source file: {src_path.name}
Source title: {source_title(src_md, src_path.stem)}

Requirements:
- Produce valid JSON only, no markdown fence.
- JSON keys: english_title, english_article, japanese_title, japanese_article, linkedin_post, tumblr_excerpt.
- english_article: 900-1400 words, Markdown, practical developer style. Target Dev.to/WordPress.
- japanese_article: 700-1100 Japanese characters/words equivalent, Markdown, practical Zenn style.
- linkedin_post: <= 1300 characters, professional, include GitHub link with LinkedIn UTM.
- tumblr_excerpt: 300-600 words, HTML-free Markdown excerpt.
- Main GitHub link must use: {GITHUB_REPO_URL}?utm_source={{platform}}&utm_medium={{article_or_social}}&utm_campaign={CAMPAIGN}
- Keep API endpoints unchanged and without UTM:
  https://cn.crazyrouter.com
  https://cn.crazyrouter.com/v1
- Brand spelling: Crazyrouter.
- Do not say "中国"; use "国内" when needed.
- Do not invent benchmark numbers.
- Include one code block if relevant.

SOURCE ARTICLE:
---
{src_md[:18000]}
---
""".strip()


def parse_json(text: str):
    text = text.strip()
    if text.startswith('```'):
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
    return json.loads(text)


def rewrite_article(src_path: Path, idx: int, dry_run=False):
    src_md = src_path.read_text()
    prompt = make_prompt(src_path, src_md, idx)
    if dry_run and os.environ.get('SKIP_LLM_IN_DRY_RUN') == '1':
        title = source_title(src_md, src_path.stem)
        return {
            'english_title': f'Claude Code Guide Daily {idx}: {title}',
            'english_article': f'# Claude Code Guide Daily {idx}\n\nSource: {src_path.name}\n\n{src_md[:3000]}',
            'japanese_title': f'Claude Code 実践ガイド {idx}',
            'japanese_article': f'この記事は Claude Code Guide の第 {idx} 回です。\n\n{GITHUB_REPO_URL}?utm_source=zenn&utm_medium=article&utm_campaign={CAMPAIGN}',
            'linkedin_post': f'Claude Code Guide daily #{idx}: {title}\n\n{GITHUB_REPO_URL}?utm_source=linkedin&utm_medium=social&utm_campaign={CAMPAIGN}',
            'tumblr_excerpt': f'Claude Code Guide daily #{idx}: {title}\n\n{GITHUB_REPO_URL}?utm_source=tumblr&utm_medium=article&utm_campaign={CAMPAIGN}'
        }
    return parse_json(call_llm(prompt))


def frontmatter_devto(title, body, slug):
    return f"""---
title: {title[:120]}
published: true
description: Daily Claude Code guide rewrite covering practical setup, API routing, and AI coding workflows.
tags: ai, claude, coding, api
canonical_url: {GITHUB_REPO_URL}?utm_source=devto&utm_medium=article&utm_campaign={CAMPAIGN}
---

{body}
"""


def frontmatter_zenn(title, body):
    safe = title.replace('"', '\\"')[:80]
    return f"""---
title: \"{safe}\"
emoji: \"🤖\"
type: \"tech\"
topics: [\"claudecode\", \"ai\", \"api\", \"crazyrouter\"]
published: true
---

{body}
"""


def md_to_html(md: str) -> str:
    lines = md.splitlines(); out=[]; in_ul=False
    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append('</ul>'); in_ul=False
    def inline(s):
        s=html.escape(s.strip())
        s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        return s
    i=0
    while i < len(lines):
        line=lines[i]
        if line.startswith('```'):
            close_ul(); i+=1; code=[]
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]); i+=1
            out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>'); i+=1; continue
        if line.startswith('# '): close_ul(); out.append('<h1>'+inline(line[2:])+'</h1>')
        elif line.startswith('## '): close_ul(); out.append('<h2>'+inline(line[3:])+'</h2>')
        elif line.startswith('### '): close_ul(); out.append('<h3>'+inline(line[4:])+'</h3>')
        elif line.startswith('- '):
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append('<li>'+inline(line[2:])+'</li>')
        elif not line.strip(): close_ul()
        else: close_ul(); out.append('<p>'+inline(line)+'</p>')
        i+=1
    close_ul(); return '\n'.join(out)


def publish_devto(pkg, slug, dry_run=False):
    repo = Path('/tmp/devto-pub')
    if not repo.exists():
        return {'skipped': 'devto repo missing'}
    subprocess.run(['git', '-C', str(repo), 'pull', '--ff-only'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    path = repo / 'posts' / f'{slug}.md'
    body = pkg['english_article'].replace('utm_source={platform}', 'utm_source=devto').replace('utm_medium={article_or_social}', 'utm_medium=article')
    path.write_text(frontmatter_devto(pkg['english_title'], body, slug))
    if dry_run: return {'dry_run_file': str(path)}
    return {'push': github_push(repo, f'Publish Claude Code daily series: {slug}', [str(path.relative_to(repo))])}


def publish_zenn(pkg, slug, dry_run=False):
    repo = Path('/tmp/zenn-pub')
    if not repo.exists():
        return {'skipped': 'zenn repo missing'}
    subprocess.run(['git', '-C', str(repo), 'pull', '--ff-only'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    path = repo / 'articles' / f'{slug[:50]}.md'
    body = pkg['japanese_article'].replace('utm_source={platform}', 'utm_source=zenn').replace('utm_medium={article_or_social}', 'utm_medium=article')
    path.write_text(frontmatter_zenn(pkg['japanese_title'], body))
    if dry_run: return {'dry_run_file': str(path)}
    return {'push': github_push(repo, f'Publish Claude Code daily Zenn: {slug}', [str(path.relative_to(repo))])}


def publish_wordpress(pkg, slug, dry_run=False):
    if dry_run: return {'dry_run': True}
    w=section('WordPress.com API'); at=val(w,'Access Token'); bid=val(w,'Blog ID')
    body = pkg['english_article'].replace('utm_source={platform}', 'utm_source=wordpress').replace('utm_medium={article_or_social}', 'utm_medium=article')
    r=requests.post(f'https://public-api.wordpress.com/rest/v1.1/sites/{bid}/posts/new',headers={'Authorization':f'Bearer {at}'},data={'title':pkg['english_title'],'content':md_to_html(body),'status':'publish','tags':'Claude Code,AI Coding,Crazyrouter'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return {'url': r.json().get('URL')}


def publish_tumblr(pkg, slug, dry_run=False):
    if dry_run: return {'dry_run': True}
    t=section('Tumblr API')
    auth=OAuth1(val(t,'OAuth Consumer Key'),val(t,'OAuth Consumer Secret'),val(t,'OAuth Token'),val(t,'OAuth Token Secret'))
    body = pkg.get('tumblr_excerpt') or pkg['english_article'][:1800]
    body = body.replace('utm_source={platform}', 'utm_source=tumblr').replace('utm_medium={article_or_social}', 'utm_medium=article')
    r=requests.post('https://api.tumblr.com/v2/blog/metavi.tumblr.com/post',auth=auth,data={'type':'text','title':pkg['english_title'],'body':md_to_html(body),'tags':'Claude Code,AI Coding,Crazyrouter'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json().get('response',{})


def publish_linkedin(pkg, slug, dry_run=False):
    if dry_run: return {'dry_run': True}
    l=section('LinkedIn API (Jianfeng Xu)'); token=val(l,'Access Token'); sub=val(l,'User Sub')
    text = pkg['linkedin_post'].replace('utm_source={platform}', 'utm_source=linkedin').replace('utm_medium={article_or_social}', 'utm_medium=social')
    post={'author':f'urn:li:person:{sub}','lifecycleState':'PUBLISHED','specificContent':{'com.linkedin.ugc.ShareContent':{'shareCommentary':{'text':text},'shareMediaCategory':'NONE'}},'visibility':{'com.linkedin.ugc.MemberNetworkVisibility':'PUBLIC'}}
    r=requests.post('https://api.linkedin.com/v2/ugcPosts',headers={'Authorization':f'Bearer {token}','Content-Type':'application/json','X-Restli-Protocol-Version':'2.0.0'},json=post,timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return {'share': r.headers.get('x-restli-id') or r.text[:200]}


def run_once(publish=False, dry_run=False, index=None):
    state=json.loads(STATE.read_text())
    articles=source_articles()
    idx = index or int(state.get('next_index', 1))
    if idx > len(articles):
        return {'done': True, 'message': 'all source articles processed'}
    src=articles[idx-1]
    pkg=rewrite_article(src, idx, dry_run=dry_run)
    slug = f"claude-code-guide-daily-{idx:02d}-" + slugify(pkg['english_title'])
    day_dir=OUTDIR / f'{idx:02d}'
    day_dir.mkdir(parents=True, exist_ok=True)
    (day_dir/'source.txt').write_text(str(src.relative_to(REPO)))
    (day_dir/'package.json').write_text(json.dumps(pkg, ensure_ascii=False, indent=2))
    (day_dir/'english.md').write_text(pkg['english_article'])
    (day_dir/'japanese.md').write_text(pkg['japanese_article'])
    (day_dir/'linkedin.txt').write_text(pkg['linkedin_post'])

    result={'time': dt.datetime.now(dt.UTC).isoformat().replace('+00:00','Z'), 'index': idx, 'source': str(src.relative_to(REPO)), 'slug': slug, 'publish': publish, 'platforms': {}}
    platforms=[('devto', publish_devto), ('zenn', publish_zenn), ('wordpress', publish_wordpress), ('tumblr', publish_tumblr), ('linkedin', publish_linkedin)]
    for name, fn in platforms:
        try:
            result['platforms'][name]=fn(pkg, slug, dry_run=(dry_run or not publish))
        except Exception as e:
            result['platforms'][name+'_error']=repr(e)
        time.sleep(1)

    RESULTS.open('a').write(json.dumps(result, ensure_ascii=False) + '\n')
    if publish and not dry_run and index is None:
        state['next_index'] = idx + 1
        state['last_run'] = result['time']
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--publish', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--index', type=int)
    args=ap.parse_args()
    res=run_once(publish=args.publish, dry_run=args.dry_run, index=args.index)
    print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
