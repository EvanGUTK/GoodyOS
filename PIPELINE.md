# GoodyOS — Repository Structure & Build Pipeline

This document maps the **Project Bible** file layout to this repo and describes the ISO build flow.

## Directory Tree

```
goodyos/  (repo root)
├── README.md
├── PIPELINE.md
├── build.sh                 # One-click: runs auto/build
├── auto/
│   ├── config              # live-build config (Bookworm, amd64, KDE)
│   ├── build               # lb config && sudo lb build
│   └── clean               # sudo lb clean --purge
├── config/
│   ├── package-lists/      # .list.chroot — what gets installed
│   │   ├── base.list.chroot
│   │   ├── desktop.list.chroot
│   │   ├── security.list.chroot
│   │   ├── dev.list.chroot
│   │   ├── ai-dev.list.chroot
│   │   ├── forensics.list.chroot
│   │   └── productivity.list.chroot
│   ├── hooks/
│   │   └── live/           # Run during chroot build
│   │       ├── 01-kde-theme.hook.chroot
│   │       ├── 02-privacy-hardening.hook.chroot
│   │       ├── 03-strip-telemetry.hook.chroot
│   │       ├── 04-mullvad-config.hook.chroot
│   │       └── 05-ghost-install.hook.chroot
│   ├── includes.chroot/    # Files copied into the OS image
│   │   ├── etc/            # hosts, nftables.conf, skel
│   │   ├── usr/share/      # wallpapers, themes
│   │   └── opt/ghost/      # Filled by 05-ghost-install from ghost/
│   ├── includes.binary/    # Boot-time (GRUB, etc.)
│   │   └── bootloaders/grub-pc/config.cfg
│   └── preseed/
│       └── goody.cfg       # Installer defaults
├── ghost/                  # Ghost app source (copied to includes or /opt at build)
│   ├── ghost.py            # GTK GUI
│   ├── ghost.sh            # Master spoof controller
│   ├── ghost.service       # systemd unit
│   ├── usb_watchdog.py     # Dead man's switch
│   └── modules/
│       ├── mac_spoof.sh
│       ├── hostname_spoof.sh
│       ├── timezone_spoof.sh
│       ├── hardware_spoof.sh
│       ├── dns_config.sh
│       ├── kill_switch.sh
│       └── scorched_earth.sh
├── docs/
│   ├── roadmap.md
│   ├── package-rationale.md
│   ├── theming-spec.md
│   ├── ghost-architecture.md
│   └── user-guide.md
└── branding/
    └── (logo, wallpaper, boot-splash)
```

## Build Pipeline (ISO)

1. **Host:** Parrot OS or Debian-based (not Windows/macOS). Install: `live-build debootstrap squashfs-tools xorriso`.
2. **Configure:** `lb config` (or run `./auto/config` which invokes it with GoodyOS options).
3. **Build:** `sudo lb build` (or `./build.sh`).
   - **Bootstrap:** debootstrap fetches minimal Debian.
   - **Chroot:** Packages from `config/package-lists/*.list.chroot` are installed.
   - **Hooks:** Scripts in `config/hooks/live/*.hook.chroot` run in order (theming, hardening, telemetry strip, Mullvad, Ghost install).
   - **Includes:** `includes.chroot/` and `includes.binary/` are merged into the image.
   - **Squash + ISO:** Filesystem is squashed and wrapped into the ISO.
4. **Output:** `live-image-amd64.hybrid.iso` (or similar) — boot in VirtualBox or burn for bare metal.
5. **Clean between builds:** `sudo ./auto/clean` then `sudo lb build`.

## Daily Loop

1. Edit config, package lists, or hooks.
2. `sudo ./auto/clean && sudo ./build.sh`
3. Boot new ISO in VirtualBox (Linux 64-bit, Debian-based, ≥4 GB RAM).
4. Test tools, Ghost tiers, kill switch, wipe.
5. Fix → commit → repeat.

## References

- **README.md** — project overview, principles, stack, Ghost levels, Scorched Earth, build quick ref.
- **GoodyOS_Project_Bible.pdf** — full spec, repo structure, Master Todo (Phases 1–12), sustainability.
- **docs/roadmap.md** — phase checklist aligned with the Bible.

GoodyOS — Build it. Ship it. Protect people.
