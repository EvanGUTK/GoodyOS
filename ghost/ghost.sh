#!/usr/bin/env bash
# GoodyOS Ghost — master identity/spoof controller
# Called at boot, on network connect, and on user "New Identity"
# Level 1: MAC, hostname, DNS, VPN kill switch, timezone
# Level 2: + Tor+Mullvad chain, hardware spoof, /proc /sys hardening
# Level 3: + dead man's switch armed, Scorched Earth ready

set -e
GHOST_ROOT="${GHOST_ROOT:-/opt/ghost}"
LEVEL="${1:-1}"

export GHOST_LEVEL="$LEVEL"
MODULES="$GHOST_ROOT/modules"

run_module() {
  local m="$1"
  [ -x "$MODULES/$m" ] && "$MODULES/$m" "$LEVEL" || true
}

# Level 1 — always
run_module mac_spoof.sh
run_module hostname_spoof.sh
run_module timezone_spoof.sh
run_module dns_config.sh
run_module kill_switch.sh

# Level 2+
if [ "$LEVEL" -ge 2 ]; then
  run_module hardware_spoof.sh
fi

# Level 3: dead man's switch and Scorched Earth are handled by usb_watchdog and GUI
echo "[Ghost] Identity applied (level $LEVEL)"
