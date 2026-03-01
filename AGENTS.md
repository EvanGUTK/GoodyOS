# GoodyOS — Agent Memory

Context for AI assistants when coding in this repo.

## Learned User Preferences

- Prefer a very descriptive README for the GoodyOS distro; use the Project Bible (GoodyOS_Project_Bible.pdf) as the source of truth when it exists (currently in parent folder: `/home/usaas/Desktop/GoodyOS/GoodyOS_Project_Bible.pdf`).
- When returning for coding, update skills and memory (e.g. AGENTS.md and .cursor/rules) so context persists.

## Learned Workspace Facts

- GoodyOS is a Debian Bookworm–based privacy Linux distro with KDE Plasma, built with live-build; build on Parrot OS or Debian-based host, not Windows or macOS.
- Canonical project spec is in GoodyOS_Project_Bible.pdf (parent of repo); README.md in repo is the main entry doc and should stay aligned with the Bible.
- Stack: Bash for automation, Python + GTK for Ghost app, nftables + UFW for firewall, Mullvad VPN, Ghost tiers 1–3, Scorched Earth wipe (NIST 800-88 / DoD), USB dead man’s switch.
- Repo layout: config/ and auto/ for live-build, package lists (*.list.chroot), hooks/, includes.chroot/ and includes.binary/, preseed/, ghost/ (Ghost app + systemd), docs/, branding/; build script is build.sh.
- IDE of choice for this project: Cursor; version control: Git with GitHub (private repo).
- Target quality: zero telemetry, zero bloat, privacy by default, proven tools only; document what GoodyOS cannot protect against.
