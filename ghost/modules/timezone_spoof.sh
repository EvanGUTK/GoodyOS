#!/usr/bin/env bash
# Ghost — timezone spoofed to decoy location (Level 1)
# Default decoy: UTC or a common neutral TZ

set -e
DECOY_TZ="${GHOST_TZ:-UTC}"
ln -sf "/usr/share/zoneinfo/$DECOY_TZ" /etc/localtime 2>/dev/null || true
echo "[Ghost] Timezone set to $DECOY_TZ"
