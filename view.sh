#!/usr/bin/env bash

PORT="${PORT:-${port:-1313}}"
URL="http://localhost:${PORT}/"

# Use China Go module proxy to avoid GitHub TLS issues
export GOPROXY=https://goproxy.cn,direct
export GOSUMDB=off
export GO111MODULE=on

# Print an OSC 8 clickable hyperlink for terminals that support it
printf '\033]8;;%s\033\\Preview URL: %s\033]8;;\033\\\n' "$URL" "$URL"

# Auto-open browser on macOS
if [[ "$OSTYPE" == darwin* ]]; then
  (sleep 2 && open "$URL") &
fi

hugo server \
  --baseURL "$URL" \
  --disableFastRender \
  --printI18nWarnings \
  --bind 127.0.0.1 \
  -p "$PORT"
