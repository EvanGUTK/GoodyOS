# GoodyOS Roadmap

Aligned with the **GoodyOS Project Bible** Master Todo (Phases 1–12).

## Phase 1 — Setup ✅
- [x] Create repo structure (this workspace)
- [ ] Clone on Parrot OS build host, install live-build deps
- [ ] First commit: initial project structure

## Phase 2 — Branding & Identity
- [ ] GoodyOS logo (Inkscape)
- [ ] Default dark wallpaper
- [ ] GRUB boot theme
- [ ] Color palette

## Phase 3 — Core Configuration
- [ ] Validate auto/config (Bookworm, amd64, KDE)
- [ ] First test build: base + desktop only
- [ ] Boot ISO in VirtualBox, confirm KDE

## Phase 4 — Package Lists
- [ ] Validate all package lists (security, forensics, dev, ai-dev, productivity)
- [ ] Rebuild and confirm tools present

## Phase 5 — Privacy & Hardening
- [ ] Custom /etc/hosts (telemetry blocks)
- [ ] UFW + nftables kill switch
- [ ] Strip telemetry packages
- [ ] DNS-over-HTTPS, sysctl, AppArmor, RAM/swap wipe on shutdown

## Phase 6 — Ghost App
- [ ] Implement all spoof modules (mac, hostname, timezone, hardware, dns, kill_switch)
- [ ] scorched_earth.sh full sequence (NIST / DoD)
- [ ] usb_watchdog.py dead man's switch
- [ ] Ghost GTK GUI + tray icon
- [ ] ghost.service and testing in VM

## Phase 7 — Mullvad Integration
- [ ] Mullvad repo, pre-config, Tor chaining for Level 2
- [ ] Test kill switch (no leaks on disconnect)

## Phase 8 — KDE Theming
- [ ] Dark theme, macOS-style dock, wallpaper, Konsole profile
- [ ] Theme hook runs at build time

## Phase 9 — Installer
- [ ] Calamares branding, preseed/goody.cfg
- [ ] Test full install in VirtualBox

## Phase 10 — QA & Polish
- [ ] Tool QA, RAM <800MB idle, wipe tests, firewall/DNS/VPN/Ghost tests
- [ ] ISO size target

## Phase 11 — Documentation
- [ ] README (done), user guide, Ghost manual, install instructions, AI protection doc

## Phase 12 — Release
- [ ] GoodyOS 1.0 Beta, clean build, GitHub Releases, go public
