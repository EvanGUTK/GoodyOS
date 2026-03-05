# GoodyOS

**A user-first privacy Linux distribution.**  
Built on **Debian Bookworm** · **KDE Plasma** · **Ghost Privacy System**

*Your machine. Your data. Nobody else's business.*

---

## What GoodyOS Is

GoodyOS is a Linux distribution built for security professionals, AI developers, software engineers, government forensic analysts, and privacy-conscious users. It is **not** another Kali reskin. Privacy is **automatic**, **invisible**, and **always on** — you do not need to be a technical expert to be protected.

### Core Principles

| Principle | Meaning |
|-----------|---------|
| **Zero Bloat** | Only tools you knowingly chose are included. Nothing hidden, nothing extra. |
| **Zero Telemetry** | No phone-home, no crash reporters, no data collection. Ever. |
| **AI Training Protection** | Your code, files, and activity never leave your machine or train any AI model. |
| **Privacy By Default** | Every privacy protection is on by default. No configuration required. |
| **Proven Trust** | Every tool has a track record. No marketing claims — only proven results. |

Implementation details and verification checklists: **docs/CORE_PRINCIPLES.md**.

---

## Technology Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| **Base OS** | Debian Bookworm | Stable, massive package ecosystem, live-build support |
| **Kernel** | Linux Hardened | Hardened patches, reduced attack surface |
| **Desktop** | KDE Plasma | Highly customizable, can look clean/minimal, lightweight |
| **Build Tool** | live-build | Official Debian ISO tool, reproducible builds |
| **VPN** | Mullvad | Proven no-log (servers seized, nothing found) |
| **Firewall** | nftables + UFW | Kernel-level kill switch, cannot be bypassed |
| **DNS** | DNS-over-HTTPS | Encrypted queries; ISP cannot see lookups |
| **Wipe** | NIST 800-88 / DoD | Government-grade secure erase standards |
| **Ghost (app)** | Python + GTK | Native Linux, lightweight GUI |
| **Automation** | Bash | Universal on Linux, ideal for system scripts |
| **IDE** | Cursor | AI-assisted; great for config and shell scripting |
| **Version Control** | Git + GitHub (private) | Full history, collaboration-ready |

---

## Desktop Environment — KDE Plasma

KDE Plasma was chosen for customization, a clean/minimal look (e.g. macOS-style), and low resource use — often lighter than GNOME.

- **Dark theme by default** — security and dev aesthetic
- **macOS-style bottom dock** — Latte Dock or KDE built-in panel
- **GoodyOS branding** — wallpaper, icons, boot splash, login screen
- **Konsole** — clean dark profile pre-configured
- **Virtual desktops and tiling** for power users
- **Target idle RAM:** under 800 MB on clean boot

---

## Ghost Privacy System

**Ghost** is GoodyOS’s identity and privacy layer. It randomizes and spoofs your digital fingerprint, runs as a systemd service, and is controlled via a GTK GUI with a system tray icon.

### Ghost Level 1 — Daily Driver

- MAC address randomized on every boot and every network connection (macchanger)
- Hostname randomly generated on every boot
- DNS-over-HTTPS (e.g. Quad9) — ISP cannot see DNS queries
- Mullvad VPN pre-installed and auto-configured
- Kernel-level nftables kill switch — if VPN drops, all traffic stops
- Timezone spoofed to decoy location
- Basic browser fingerprint protection system-wide

### Ghost Level 2 — Elevated

- Everything in Level 1, plus:
- **Tor + Mullvad chained:** You → Mullvad → Tor → destination
- Hardware identifiers spoofed at OS level (CPU, GPU, drive serials, monitor EDID)
- WebGL and Canvas fingerprinting mitigated system-wide
- Application logs disabled
- No write to disk except encrypted volumes
- Screen resolution and monitor EDID spoofed
- `/proc` and `/sys` hardened — apps cannot read real hardware IDs

### Ghost Level 3 — Scorched Earth Ready

- Everything in Level 2, plus:
- RAM encryption fully active
- **Dead man’s switch** armed and monitoring a registered USB drive
- All system logs disabled
- Kernel hardened (no core dumps, no debugging interfaces)
- Network isolated except through Mullvad + Tor
- Scorched Earth kill switch armed
- RAM-only session mode — no write to disk

### Ghost Architecture

- **Python + GTK** app with a systemd background service
- GUI: current Ghost level, identity status, VPN status, one-click **New Identity**
- System tray icon shows current level
- **Boot:** full identity randomization (MAC, hostname, timezone, hardware spoof)
- **Network connect:** new MAC and hostname generated automatically
- **User request:** manual re-ghost via GUI or shortcut
- **USB removal:** if dead man’s switch is armed, triggers Scorched Earth immediately

---

## Scorched Earth — Emergency Wipe

Scorched Earth is the nuclear option: it makes the machine forensically unrecoverable before anyone can intervene. Supports **NIST 800-88** (fast, SSD-optimized) and **DoD 5220.22-M** (7-pass, thorough). User chooses at setup.

### Trigger Options

- Hotkey hold (e.g. hold F12 for 3 seconds)
- Optional **USB dead man’s switch** — remove USB drive → wipe runs automatically
- Ghost GUI panic button
- Remote encrypted trigger from phone (optional)

### Wipe Sequence

1. All network interfaces killed — no traffic in or out  
2. All running processes terminated  
3. RAM overwritten with zeros — encryption keys destroyed  
4. NIST 800-88 crypto erase (SSDs, seconds) or DoD 7-pass (HDDs)  
5. Bootloader overwritten — machine will not boot  
6. Partition table destroyed  
7. Result: forensically unrecoverable  

SSDs with NIST 800-88 crypto erase finish in seconds; HDDs with DoD 7-pass take longer. Users should know their disk type at setup.

---

## USB Dead Man’s Switch

You carry a **registered USB drive**. A GoodyOS service checks for it every few seconds. If it is removed while **Ghost Level 3** is armed, **Scorched Earth runs automatically** — no button press.

- USB registered during GoodyOS setup
- systemd service polls every 2–3 seconds
- USB present → normal operation
- USB removed while Level 3 armed → Scorched Earth triggers immediately
- USB removed at Level 1 or 2 → notification only, no wipe
- Arm/disarm via Ghost GUI or tray icon

---

## Mullvad VPN Integration

Mullvad is the default and only recommended VPN.

- **Proven no-log:** Dutch police seized Mullvad servers; no logs found
- **Anonymous signup:** no email; account is a random number
- **Anonymous payment:** cash by mail, Monero
- **Open source:** client audited
- **Kill switch:** GoodyOS adds a **kernel-level nftables** kill switch on top of Mullvad’s — if Mullvad drops, traffic stops at the kernel
- **Tor chaining:** Ghost Level 2+ routes You → Mullvad → Tor → destination

---

## AI Training Protection

GoodyOS guarantees: **your code and data do not leave your machine and are not used to train any AI model.** Enforced at the network level.

- **Hosts file** blocks known AI/data-collection endpoints (OpenAI, Google, Meta, Microsoft, Amazon, Apple, etc.)
- Network rules prevent silent background uploads
- No cloud sync enabled by default
- **Ollama** pre-configured for local LLM inference
- AI coding assistance possible without sending code off-device
- Hosts file updated with each release as new endpoints are discovered

---

## Security & Privacy Hardening

| Feature | Detail |
|---------|--------|
| **UFW Firewall** | All inbound blocked by default; outbound restricted |
| **nftables Kill Switch** | Kernel-level; cannot be bypassed by crashing apps |
| **DNS-over-HTTPS + DNSSEC** | Encrypted, verified DNS; ISP blind to lookups |
| **RAM Wipe on Shutdown** | RAM overwritten on every shutdown (cold-boot resistance) |
| **Swap** | Encrypted and wiped on shutdown |
| **AppArmor** | Mandatory access control for pre-installed apps |
| **Spectre/Meltdown** | Mitigations enabled |

---

## Software Stack (Package Lists)

- **base** — minimal Debian core  
- **desktop** — KDE Plasma + Latte Dock  
- **security** — penetration testing tools  
- **dev** — dev tools, Docker, Git  
- **ai-dev** — Python ML, Ollama, Jupyter, CUDA  
- **forensics** — nwipe, Autopsy, Testdisk  
- **productivity** — LibreOffice, VLC, GIMP, etc.  

---

## Repo & Build Overview

- **Build:** Debian **live-build** on a **Parrot OS** (or Debian-based) host — not Windows or macOS.
- **Output:** `live-image-amd64.hybrid.iso` for live boot and install.
- **Daily loop:** edit config, package lists, or hooks → `sudo ./auto/clean && sudo ./build.sh` → test ISO in VirtualBox.

**Repository layout:** See **PIPELINE.md** for the full directory tree and build flow. Key areas: `auto/` (config, build, clean), `config/package-lists/*.list.chroot`, `config/hooks/live/`, `config/includes.chroot/` (hosts, nftables, skel, wallpapers, themes), `config/includes.binary/` (GRUB), `config/preseed/`, and `ghost/` (Ghost app source and systemd unit).

---

## What GoodyOS Cannot Protect Against

Documented so the threat model is clear:

- Physical seizure **before** Scorched Earth completes  
- Hardware implants installed by an adversary  
- You voluntarily logging into personal accounts (Google, Microsoft, etc.)  
- Nation-state timing analysis at scale over long periods  
- Subpoenas before Mullvad is connected  
- BIOS/UEFI-level firmware attacks  
- Physical side-channel attacks  

GoodyOS is not “unbreakable by a nation-state with unlimited resources and physical access.” It aims to make **remote surveillance and fingerprinting** effectively impossible for the vast majority of real-world scenarios, and to ensure that if the machine is seized, **Scorched Earth has already run.**

---

## Build Quick Reference

```bash
# Dependencies (Debian/Parrot host)
sudo apt install live-build debootstrap squashfs-tools xorriso

# Optional: Mullvad repo key (needed for mullvad-vpn package)
./auto/setup-archives

# Full build (runs lb config, syncs Ghost, then lb build)
sudo ./build.sh

# Clean between builds
sudo ./auto/clean
```

**Technology Stack:** See **docs/TECHNOLOGY_STACK.md** (Base OS, kernel, desktop, VPN, firewall, DNS, wipe, Ghost).

Test in VirtualBox: Linux 64-bit, Debian-based, ≥4 GB RAM (8 GB for AI dev), mount the built ISO, boot live, then test tools, Ghost tiers, kill switch, and wipe. Keep ≥50 GB free on the build machine.

---

**GoodyOS — Build it. Ship it. Protect people.**
