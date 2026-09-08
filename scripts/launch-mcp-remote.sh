#!/bin/sh

set -eu

# Claude Desktop may pass ordinary ${VAR:-default} arguments literally.
default_mcp_url=${1:-http://127.0.0.1:8765/mcp}
mcp_url=${KLAYOUT_MCP_URL:-$default_mcp_url}

exec npx -y mcp-remote "$mcp_url" --allow-http
