#!/usr/bin/env bash
set -euo pipefail
CRON_LINE="17 9 * * * cd /root/.openclaw/workspace/claude-code-guide && /usr/bin/python3 promotion/daily_rewrite_publish.py --publish >> /root/.openclaw/workspace/claude-code-guide/logs/daily_rewrite_publish.log 2>&1"
( crontab -l 2>/dev/null | grep -v 'promotion/daily_rewrite_publish.py --publish' ; echo "$CRON_LINE" ) | crontab -
echo "Installed daily cron: $CRON_LINE"
