# GoodyOS Package Rationale

Why each package list exists and how it supports **Zero Bloat** and **Proven Trust**. See **README.md** and **docs/CORE_PRINCIPLES.md** for the full principle set.

| List | Purpose | Proven Trust note |
|------|---------|-------------------|
| **base** | Minimal Debian core: kernel, network, init, nftables. No desktop, no telemetry. | Debian: stable, reproducible, live-build support; nftables: kernel-level, auditable. |
| **desktop** | KDE Plasma, Latte Dock, Konsole, Dolphin — daily driver DE. | KDE: open source, highly customizable, often lighter than GNOME; long track record. |
| **security** | Nmap, Wireshark, aircrack-ng, macchanger, UFW, Mullvad VPN. | Mullvad: no-log **proven** (servers seized, nothing found). UFW/nftables: standard, kernel-level. |
| **dev** | build-essential, Git, Docker, Python 3 + GI for Ghost. | Git/Docker/Python: industry standard, auditable. |
| **ai-dev** | Ollama, Jupyter, Python ML stack; optional CUDA. | Local LLM only — no code leaves machine; aligns with AI Training Protection. |
| **forensics** | nwipe (DoD/NIST), Autopsy, Testdisk, Foremost. | nwipe: NIST 800-88 and DoD 5220.22-M; government-grade wipe. |
| **productivity** | LibreOffice, VLC, Thunderbird, GIMP, Inkscape, Kdenlive, Firefox ESR. | FOSS replacements; no cloud lock-in by default. |

All choices follow **Zero Bloat** (only what is listed) and **Proven Trust** (track record, no marketing-only claims). See **docs/CORE_PRINCIPLES.md** for implementation checklists.
