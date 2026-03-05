# Ghost Architecture

Ghost is GoodyOS’s identity and privacy layer: systemd service + Python/GTK GUI.

## Components
- **ghost.sh** — Master script: runs at boot and on “New Identity”; calls modules.
- **modules/** — mac_spoof, hostname_spoof, timezone_spoof, hardware_spoof (L2+), dns_config, kill_switch, scorched_earth.
- **usb_watchdog.py** — Dead man’s switch: poll USB; if L3 armed and USB removed → Scorched Earth.
- **ghost.py** — GUI: level selector, status, New Identity, panic button; tray icon.
- **ghost.service** — systemd: runs ghost.sh at boot.

## Levels
- **1 — Daily Driver:** MAC/hostname/TZ spoof, DoH, Mullvad, kill switch.
- **2 — Elevated:** + Tor+Mullvad chain, hardware spoof, /proc/sys hardening, no disk write except encrypted.
- **3 — Scorched Earth Ready:** + USB dead man’s switch armed, RAM-only, full lockdown.

Build order (from Bible): spoof scripts → nftables → scorched_earth → usb_watchdog → ghost.sh → GUI → tray → test in VM.
