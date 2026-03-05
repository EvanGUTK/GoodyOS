#!/usr/bin/env bash
# Ghost — MAC address randomization (Level 1)
# Every boot and every network connection

set -e
LEVEL="${1:-1}"

if ! command -v macchanger >/dev/null 2>&1; then
  echo "[Ghost] macchanger not installed, skip MAC spoof"
  exit 0
fi

for iface in /sys/class/net/*; do
  [ -d "$iface" ] || continue
  name="$(basename "$iface")"
  [[ "$name" == "lo" ]] && continue
  macchanger -r "$name" 2>/dev/null || true
done

echo "[Ghost] MAC addresses randomized"
