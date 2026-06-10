#!/usr/bin/env python3
import json, re, time, html, requests
from pathlib import Path
from requests_oauthlib import OAuth1

ROOT=Path('/root/.openclaw/workspace')
REPO=ROOT/'claude-code-guide'
TOOLS=(ROOT/'TOOLS.md').read_text()
OUT=REPO/'promotion/publish-results.json'
OUT.parent.mkdir(parents=True, exist_ok=True)
CAMPAIGN='claude_code_guide'
GITHUB='https://github.com/xujfcn/claude-code-guide'
TITLE='Claude Code Guide: Practical Setup, API Routing, and AI Coding Workflows'

def section(name):
    idx=TOOLS.find('## '+name)
    if idx<0: return ''
    nxt=TOOLS.find('\n## ',idx+1)
    return TOOLS[idx:nxt if nxt!=-1 else len(TOOLS)]

def val(block,key):
    m=re.search(r'- \*\*'+re.escape(key)+r'\*\*:\s*(.+)', block)
    return m.group(1).strip() if m else None

def inline(s):
    s=html.escape(s.strip())
    s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

def md_to_html(md):
    lines=md.splitlines(); out=[]; in_ul=False
    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append('</ul>'); in_ul=False
    i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('```'):
            close_ul(); i+=1; code=[]
            while i<len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]); i+=1
            out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>'); i+=1; continue
        if line.startswith('### '): close_ul(); out.append('<h3>'+inline(line[4:])+'</h3>')
        elif line.startswith('## '): close_ul(); out.append('<h2>'+inline(line[3:])+'</h2>')
        elif line.startswith('# '): close_ul(); out.append('<h1>'+inline(line[2:])+'</h1>')
        elif line.startswith('- '):
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append('<li>'+inline(line[2:])+'</li>')
        elif not line.strip(): close_ul()
        else: close_ul(); out.append('<p>'+inline(line)+'</p>')
        i+=1
    close_ul(); return '\n'.join(out)

def body_after_marker(path, marker):
    s=path.read_text()
    if marker in s:
        s=s.split(marker,1)[1].strip()
    return s

def publish_linkedin():
    block=section('LinkedIn API (Jianfeng Xu)')
    token=val(block,'Access Token'); sub=val(block,'User Sub')
    text=(REPO/'promotion/linkedin-post.md').read_text().split('## 02｜LinkedIn 推广帖',1)[-1].strip()
    post={
      'author':f'urn:li:person:{sub}',
      'lifecycleState':'PUBLISHED',
      'specificContent':{'com.linkedin.ugc.ShareContent':{'shareCommentary':{'text':text},'shareMediaCategory':'NONE'}},
      'visibility':{'com.linkedin.ugc.MemberNetworkVisibility':'PUBLIC'}
    }
    r=requests.post('https://api.linkedin.com/v2/ugcPosts',headers={'Authorization':f'Bearer {token}','Content-Type':'application/json','X-Restli-Protocol-Version':'2.0.0'},json=post,timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.headers.get('x-restli-id') or r.text[:300]

def publish_mastodon():
    block=section('Mastodon (@xujfcn@mastodon.social)')
    token=val(block,'Access Token')
    text=(REPO/'promotion/mastodon-post.md').read_text().split('## 03｜Mastodon 推广帖',1)[-1].strip()
    r=requests.post('https://mastodon.social/api/v1/statuses',headers={'Authorization':f'Bearer {token}'},data={'status':text,'visibility':'public'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json().get('url')

def publish_bluesky():
    block=section('Bluesky (@xujfcn.bsky.social)')
    handle=val(block,'Handle'); password=val(block,'App Password')
    text=(REPO/'promotion/bluesky-post.md').read_text().split('## 04｜Bluesky 推广帖',1)[-1].strip()
    # Bluesky has 300 char limit; use compact version with UTM link.
    text='Claude Code setup gets confusing fast: root endpoint or /v1?\n\n36+ article Chinese guide for Claude Code + Crazyrouter: setup, Base URL rules, troubleshooting, PRD-to-code, Figma, Mermaid.\n\nhttps://github.com/xujfcn/claude-code-guide?utm_source=bluesky&utm_medium=social&utm_campaign=claude_code_guide'
    auth=requests.post('https://bsky.social/xrpc/com.atproto.server.createSession',json={'identifier':handle,'password':password},timeout=60)
    if not auth.ok: raise RuntimeError(f'auth {auth.status_code} {auth.text[:500]}')
    sess=auth.json()
    rec={'$type':'app.bsky.feed.post','text':text,'createdAt':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    r=requests.post('https://bsky.social/xrpc/com.atproto.repo.createRecord',headers={'Authorization':'Bearer '+sess['accessJwt']},json={'repo':sess['did'],'collection':'app.bsky.feed.post','record':rec},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json()

def hashnode_content():
    md=(REPO/'promotion/devto_hashnode_article.md').read_text()
    # trim header marker
    md=md.split('### Body',1)[-1].strip()
    return md.replace('utm_source=devto','utm_source=hashnode')

def publish_hashnode():
    h=section('Hashnode API'); token=val(h,'API Token'); pub=val(h,'Publication ID')
    md=hashnode_content()
    mutation='''mutation PublishPost($input: PublishPostInput!) { publishPost(input: $input) { post { id slug url title } } }'''
    input_data={
      'publicationId': pub,
      'title': TITLE,
      'contentMarkdown': md,
      'tags': [{'name':'Claude Code','slug':'claude-code'}, {'name':'AI Coding','slug':'ai-coding'}, {'name':'Developer Tools','slug':'developer-tools'}, {'name':'API Gateway','slug':'api-gateway'}],
      'seo': {'title': TITLE, 'description':'A practical Claude Code guide repo covering setup, Crazyrouter routing, Base URL rules, and AI coding workflows.'},
    }
    r=requests.post('https://gql.hashnode.com',headers={'Authorization':token,'Content-Type':'application/json'},json={'query':mutation,'variables':{'input':input_data}},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    data=r.json()
    if data.get('errors'): raise RuntimeError(str(data['errors'])[:800])
    return data

def blogger_access():
    b=section('Google Blogger API')
    r=requests.post('https://oauth2.googleapis.com/token',data={'client_id':val(b,'OAuth Client ID'),'client_secret':val(b,'OAuth Client Secret'),'refresh_token':val(b,'Refresh Token'),'grant_type':'refresh_token'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json()['access_token'], val(b,'Blog ID')

def publish_blogger():
    at,bid=blogger_access()
    md=hashnode_content().replace('utm_source=hashnode','utm_source=blogger')
    r=requests.post(f'https://www.googleapis.com/blogger/v3/blogs/{bid}/posts/',headers={'Authorization':f'Bearer {at}','Content-Type':'application/json'},json={'kind':'blogger#post','title':TITLE,'content':md_to_html(md),'labels':['Claude Code','AI Coding','Developer Tools','Crazyrouter']},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json().get('url')

def publish_wordpress():
    w=section('WordPress.com API'); at=val(w,'Access Token'); bid=val(w,'Blog ID')
    md=hashnode_content().replace('utm_source=hashnode','utm_source=wordpress')
    r=requests.post(f'https://public-api.wordpress.com/rest/v1.1/sites/{bid}/posts/new',headers={'Authorization':f'Bearer {at}'},data={'title':TITLE,'content':md_to_html(md),'status':'publish','tags':'Claude Code,AI Coding,Developer Tools,Crazyrouter'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json().get('URL')

def publish_tumblr():
    t=section('Tumblr API')
    auth=OAuth1(val(t,'OAuth Consumer Key'),val(t,'OAuth Consumer Secret'),val(t,'OAuth Token'),val(t,'OAuth Token Secret'))
    md=hashnode_content().replace('utm_source=hashnode','utm_source=tumblr')
    body=md_to_html('\n'.join(md.splitlines()[:80]))
    r=requests.post('https://api.tumblr.com/v2/blog/metavi.tumblr.com/post',auth=auth,data={'type':'text','title':TITLE,'body':body,'tags':'Claude Code,AI Coding,Developer Tools,Crazyrouter'},timeout=60)
    if not r.ok: raise RuntimeError(f'{r.status_code} {r.text[:500]}')
    return r.json().get('response',{})

publishers=[
  ('linkedin', publish_linkedin),
  ('mastodon', publish_mastodon),
  ('bluesky', publish_bluesky),
  ('hashnode', publish_hashnode),
  ('blogger', publish_blogger),
  ('wordpress', publish_wordpress),
  ('tumblr', publish_tumblr),
]

log={}
for name,fn in publishers:
    try:
        print('publishing', name, flush=True)
        log[name]=fn()
        print(name, 'OK', log[name], flush=True)
    except Exception as e:
        log[name+'_error']=repr(e)
        print(name, 'ERR', e, flush=True)
    time.sleep(1)
OUT.write_text(json.dumps(log, ensure_ascii=False, indent=2))
print(json.dumps(log, ensure_ascii=False, indent=2))
