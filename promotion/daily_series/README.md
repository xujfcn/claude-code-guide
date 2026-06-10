# Claude Code Guide Daily Rewrite Series

Purpose: rewrite one source article from `articles/` every day and automatically publish it to available platforms.

Source: 36 articles in this repository.

Default auto platforms:

- Dev.to via `/tmp/devto-pub` Git push
- Zenn via `/tmp/zenn-pub` Git push
- WordPress.com REST API
- Tumblr REST API
- LinkedIn social post

Currently skipped until credentials/API are fixed:

- Hashnode: GraphQL endpoint currently returns HTML instead of JSON
- Blogger: refresh token expired/revoked
- Mastodon: account login disabled
- Bluesky: account takedown

## Run manually

```bash
python3 promotion/daily_rewrite_publish.py --dry-run
python3 promotion/daily_rewrite_publish.py --publish
```

## State

- `promotion/daily_series/state.json` tracks which source index to publish next.
- Generated articles are saved under `promotion/daily_series/generated/`.
- Results are appended to `promotion/daily_series/results.jsonl`.
