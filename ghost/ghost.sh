#!/usr/bin/env bash
# GoodyOS Ghost — master identity/spoof controller
# Called at boot, on network connect, and on user "New Identity".
# Orchestrates: mac_spoof, hostname_spoof, timezone_spoof, hardware_spoof, dns_config, kill_switch

set -e
GHOST_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GHOST_LEVEL="${GHOST_LEVEL:-1}"

run_module() {
	local m="$1"
	[[ -x "$GHOST_ROOT/modules/$m" ]] && "$GHOST_ROOT/modules/$m" || true
}

case "${1:-all}" in
	all)
		run_module mac_spoof.sh
		run_module hostname_spoof.sh
		run_module timezone_spoof.sh
		[[ "$GHOST_LEVEL" -ge 2 ]] && run_module hardware_spoof.sh || true
		run_module dns_config.sh
		run_module kill_switch.sh
		;;
	mac)    run_module mac_spoof.sh ;;
	host)   run_module hostname_spoof.sh ;;
	tz)     run_module timezone_spoof.sh ;;
	hw)     run_module hardware_spoof.sh ;;
	dns)    run_module dns_config.sh ;;
	kill)   run_module kill_switch.sh ;;
	*)      echo "Usage: $0 all|mac|host|tz|hw|dns|kill" ; exit 1 ;;
esac
