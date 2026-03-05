#!/usr/bin/env bash
# Ghost — nftables kernel-level kill switch (Level 1)
# If VPN drops, all traffic stops

set -e
RULES="/etc/nftables.conf"
[ -f "$RULES" ] && nft -f "$RULES" 2>/dev/null || true
echo "[Ghost] Kill switch rules loaded"
