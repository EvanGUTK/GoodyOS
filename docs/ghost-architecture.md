# Ghost Architecture

Ghost is GoodyOS's identity and privacy layer: Python + GTK app + systemd service.

## Components
- **ghost.sh** — Master script; runs at boot and on "New Identity". Invokes modules by level.
- **modules/** — mac_spoof, hostname_spoof, timezone_spoof, dns_config, kill_switch; Level 2: hardware_spoof. scorched_earth.sh for emergency wipe.
- **ghost.py** — GTK GUI: level selector, New Identity, panic (Scorched Earth), tray icon.
- **usb_watchdog.py** — Polls for registered USB; Level 3 + removal → Scorched Earth.
- **ghost.service** — systemd oneshot at boot (runs ghost.sh 1).

## Flow
- **Boot:** Full identity randomization (MAC, hostname, timezone, Level 2: hardware spoof).
- **Network connect:** New MAC + hostname (handled by udev/net hook or Ghost service).
- **User:** Manual re-ghost via GUI or shortcut.
- **USB removal (Level 3 armed):** Scorched Earth immediately.

## Build order (from Bible)
1. Spoof scripts (MAC, hostname, timezone, hardware)
2. nftables kill switch
3. Scorched Earth script
4. USB dead man's switch service
5. ghost.sh master
6. GTK GUI + tray
7. systemd units
8. Test in VirtualBox
