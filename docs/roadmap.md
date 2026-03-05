# GoodyOS Roadmap

Aligned with the Project Bible Master Todo List.

## Phase 1 — Setup ✅
- [x] Create repo structure (this worktree)
- [x] Install live-build deps (on Parrot/Debian host)
- [x] Full folder structure and initial files
- [ ] First commit: initial project structure

## Phase 2 — Branding & Identity
- [ ] Design GoodyOS logo (Inkscape)
- [ ] Default dark wallpaper
- [ ] GRUB boot screen theme
- [ ] Color palette (primary, background, accent)
- [ ] Commit to /branding

## Phase 3 — Core Configuration
- [ ] Finalize auto/config for live-build (lb config)
- [ ] First test build: base + desktop only
- [ ] Boot ISO in VirtualBox, confirm KDE loads

## Phase 4 — Package Lists
- [ ] Validate all package lists (security, forensics, dev, ai-dev, productivity)
- [ ] Rebuild and confirm tools present and launch

## Phase 5 — Privacy & Hardening
- [ ] Custom /etc/hosts telemetry block list
- [ ] UFW firewall hook — enabled by default
- [ ] DNS-over-HTTPS (Quad9)
- [ ] nftables kill switch rules final
- [ ] sysctl hardening, AppArmor, RAM/swap wipe on shutdown
- [ ] Rebuild and verify firewall on first boot

## Phase 6 — Ghost App
- [ ] Test each Ghost module in VM
- [ ] Full Scorched Earth sequence on virtual disk (NIST vs DoD timing)
- [ ] GTK GUI polish, system tray
- [ ] USB dead man's switch registration flow

## Phase 7 — Mullvad Integration
- [ ] Mullvad repo and pre-config
- [ ] Tor + Mullvad chaining for Level 2
- [ ] Test kill switch — zero leaks on disconnect

## Phase 8 — KDE Theming
- [ ] Dark theme, macOS-style dock, GoodyOS wallpaper/icons
- [ ] Konsole dark profile, theme hook at build time

## Phase 9 — Installer
- [ ] Calamares with GoodyOS branding
- [ ] preseed/goody.cfg for default install
- [ ] Test full install in VirtualBox

## Phase 10 — QA & Polish
- [ ] Every tool tested, RAM under 800MB idle
- [ ] DoD/NIST wipe, firewall, DNS, kill switch, Ghost tiers
- [ ] ISO under 4GB

## Phase 11 — Documentation
- [ ] README, user guide, Ghost manual, install instructions
- [ ] AI training protection guarantee documented

## Phase 12 — Release
- [ ] GoodyOS 1.0 Beta
- [ ] Reproducible clean build, upload ISO, repo public
