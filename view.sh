#!/usr/bin/env bash

PORT="${PORT:-${port:-1313}}"

# Use China Go module proxy to avoid GitHub TLS issues
export GOPROXY=https://goproxy.cn,direct
export GOSUMDB=off
export GO111MODULE=on

for BIN_DIR in "$HOME/miniconda3/bin" "$HOME/.local/bin"; do
  if [[ -d "$BIN_DIR" && ":$PATH:" != *":$BIN_DIR:"* ]]; then
    export PATH="$BIN_DIR:$PATH"
  fi
done

if ! command -v hugo >/dev/null 2>&1; then
  echo "Error: hugo is not installed or not on PATH." >&2
  echo "Install Hugo Extended and rerun this script." >&2
  exit 127
fi

if ! command -v go >/dev/null 2>&1; then
  echo "Error: go is not installed or not on PATH." >&2
  echo "Install Go and rerun this script." >&2
  exit 127
fi

if [[ ! "$PORT" =~ ^[0-9]+$ ]] || (( PORT < 1 || PORT > 65535 )); then
  echo "Error: PORT must be a number from 1 to 65535." >&2
  exit 2
fi

REQUESTED_PORT="$PORT"
while (exec 3<>"/dev/tcp/127.0.0.1/$PORT") >/dev/null 2>&1; do
  if (( PORT == 65535 )); then
    echo "Error: no available port found at or above $REQUESTED_PORT." >&2
    exit 1
  fi
  ((PORT += 1))
done

if [[ "$PORT" != "$REQUESTED_PORT" ]]; then
  echo "Port $REQUESTED_PORT is in use; using $PORT instead."
fi

URL="http://localhost:${PORT}/"

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
