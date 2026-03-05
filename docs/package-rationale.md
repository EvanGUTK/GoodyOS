# GoodyOS Package Rationale

Why each stack exists (see README and Project Bible for full stack).

| List | Purpose |
|------|--------|
| **base** | Minimal Debian core; no telemetry. Stripped in 03-strip-telemetry. |
| **desktop** | KDE Plasma + Latte Dock; target &lt;800MB idle RAM. |
| **security** | Pen testing (nmap, Wireshark, Metasploit, etc.) + UFW, nftables, macchanger for Ghost. |
| **dev** | Build tools, Git, Docker, Python + GTK for Ghost. |
| **ai-dev** | Ollama, Jupyter; local LLM only — no code leaves machine. |
| **forensics** | nwipe (DoD/NIST), Autopsy, Testdisk, Volatility. |
| **productivity** | LibreOffice, VLC, Thunderbird, GIMP, etc. — FOSS replacements. |

Mullvad is added via its own repo in a later phase; Tor for Level 2.
