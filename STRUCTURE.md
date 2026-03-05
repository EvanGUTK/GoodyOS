# GoodyOS Repository Structure & Pipeline

This document maps the repo tree and how it feeds the ISO build.

## Directory Tree

```
rxm/ (GoodyOS repo)
├── README.md                 # Project overview (you are here)
├── STRUCTURE.md              # This file — tree and pipeline
├── build.sh                  # One-click build (syncs Ghost, runs lb build)
├── .gitignore
│
├── auto/                     # live-build automation
│   ├── config               # Generate/update lb config (Debian Bookworm, KDE)
│   ├── build                # sudo lb build
│   └── clean                # sudo lb clean
│
├── config/                   # live-build config (used by lb build)
│   ├── package-lists/       # .list.chroot → packages in image
│   │   ├── base.list.chroot
│   │   ├── desktop.list.chroot
│   │   ├── security.list.chroot
│   │   ├── dev.list.chroot
│   │   ├── ai-dev.list.chroot
│   │   ├── forensics.list.chroot
│   │   └── productivity.list.chroot
│   ├── hooks/
│   │   ├── live/            # Run during chroot build
│   │   │   ├── 01-kde-theme.hook.chroot
│   │   │   ├── 02-privacy-hardening.hook.chroot
│   │   │   ├── 03-strip-telemetry.hook.chroot
│   │   │   ├── 04-mullvad-config.hook.chroot
│   │   │   └── 05-ghost-install.hook.chroot
│   │   └── normal/          # Run at install time (optional)
│   ├── includes.chroot/     # Files copied into the OS image
│   │   ├── etc/hosts
│   │   ├── etc/nftables.conf
│   │   ├── etc/skel/
│   │   ├── usr/share/wallpapers/goodyos/
│   │   ├── usr/share/themes/
│   │   └── opt/ghost/       # Filled by build.sh from ghost/
│   └── includes.binary/     # Boot/binary image files
│       ├── boot/grub/theme/
│       └── bootloaders/grub-pc/config.cfg
│
├── preseed/
│   └── goody.cfg            # Auto-installer answers
│
├── ghost/                    # Ghost app source (copied to includes.chroot/opt/ghost by build.sh)
│   ├── ghost.py             # GTK GUI
│   ├── ghost.sh             # Master controller
│   ├── ghost.service
│   ├── usb_watchdog.py
│   ├── usb_watchdog.service
│   └── modules/
│       ├── mac_spoof.sh
│       ├── hostname_spoof.sh
│       ├── timezone_spoof.sh
│       ├── dns_config.sh
│       ├── kill_switch.sh
│       ├── hardware_spoof.sh
│       └── scorched_earth.sh
│
├── docs/
│   ├── roadmap.md
│   ├── package-rationale.md
│   ├── theming-spec.md
│   ├── ghost-architecture.md
│   └── user-guide.md
│
└── branding/
    ├── README.md
    ├── logo.png             # Phase 2
    ├── wallpaper.png        # Phase 2
    └── boot-splash/         # Phase 2
```

## Build Pipeline (high level)

1. **Prerequisites** (on Debian/Parrot host):  
   `sudo apt install live-build debootstrap squashfs-tools xorriso`

2. **First-time or after lb clean:**  
   Optionally run `./auto/config` to (re)generate lb config.

3. **Build:**  
   `./build.sh`  
   - Syncs `ghost/` → `config/includes.chroot/opt/ghost/`  
   - Runs `sudo lb build`  
   - Output: `live-image-amd64.hybrid.iso` (copy to `goodyos.iso`)

4. **Clean:**  
   `sudo ./auto/clean` or `./build.sh clean` then `./build.sh`

5. **Test:**  
   VirtualBox: Linux 64-bit, Debian-based, ≥4 GB RAM, mount ISO, boot live.

## Data flow

- **Package lists** → installed inside chroot during `lb build`.
- **Hooks (live)** → run inside chroot in order (01 → 05).
- **includes.chroot** → copied into the image as-is (paths relative to root).
- **includes.binary** → used in the binary (boot) image.
- **Ghost** → developed in `ghost/`, injected into image via `build.sh` into `config/includes.chroot/opt/ghost/`.

GoodyOS — *Your machine. Your data. Nobody else's business.*
