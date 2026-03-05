# GoodyOS Core Principles — Implementation

GoodyOS is built for security professionals, AI developers, software engineers, government forensic analysts, and privacy-conscious users. It is **not** another Kali reskin. **Privacy is automatic, invisible, and always on** — you do not need to be a technical expert to be protected.

This document maps each core principle to **what we do at build time and at first boot**, and how to verify it.

---

## 1. Zero Bloat

**Meaning:** Only tools you knowingly chose are included. Nothing hidden, nothing extra.

| Implementation | Where |
|----------------|--------|
| Every package is in an explicit list: `base`, `desktop`, `security`, `dev`, `ai-dev`, `forensics`, `productivity`. No "recommends" bloat unless explicitly allowed. | `config/package-lists/*.list.chroot` |
| Base list is minimal Debian core only. Desktop and tools are separate optional lists. | `config/package-lists/base.list.chroot` |
| No hidden services or pre-installed cloud sync, assistant, or optional extras. | Hooks do not install extra packages; strip-telemetry removes unneeded ones. |
| Build uses explicit package lists; no automatic "task" bundles that pull in hundreds of packages. | live-build config |

**Verification checklist**
- [ ] Review every package in each list; remove anything not intentionally chosen.
- [ ] After build, no unexpected packages (e.g. `dpkg -l` audit or manifest).
- [ ] No pre-enabled optional services (printing, Bluetooth, etc.) unless documented.

---

## 2. Zero Telemetry

**Meaning:** No phone-home, no crash reporters, no data collection. Ever.

| Implementation | Where |
|----------------|--------|
| Strip telemetry packages: `popularity-contest`, `apt-listchanges` (optional), and any crash/usage reporting. | `config/hooks/live/03-strip-telemetry.hook.chroot` |
| Disable crash reporters: Apport, Whoopsie, and similar. Disable any service that sends data off-host. | Same hook |
| Hosts file blocks known telemetry and analytics domains (Microsoft, Google, Canonical, etc.). | `config/includes.chroot/etc/hosts` |
| No crash reporter, no usage stats, no "improve your experience" dialogs. | Policy: no such packages in lists; hook removes/disabled. |

**Verification checklist**
- [ ] `popularity-contest` and similar are purged or not installed.
- [ ] No running service that sends data to third parties (inspect systemd units and cron).
- [ ] Hosts file includes telemetry domains; blocked endpoints do not resolve.

---

## 3. AI Training Protection

**Meaning:** Your code, files, and activity never leave your machine and are not used to train any AI model.

| Implementation | Where |
|----------------|--------|
| Hosts file blocks known AI/data-collection endpoints: OpenAI, Google, Meta, Microsoft, Amazon, Apple, and others. Updated with each release. | `config/includes.chroot/etc/hosts` |
| Network rules (firewall) prevent silent background uploads; no cloud sync enabled by default. | Privacy hardening hook; UFW/nftables |
| Ollama (local LLM) available so AI assistance does not require sending code off-device. | `config/package-lists/ai-dev.list.chroot` |
| Documentation states the guarantee in plain language. | README, this doc, user-guide |

**Verification checklist**
- [ ] Hosts file contains AI/ML and data-collection domains; they resolve to 127.0.0.1.
- [ ] No default cloud sync or "send to cloud" options enabled.
- [ ] User guide and README clearly state: code and activity do not leave the machine or train external AI.

---

## 4. Privacy By Default

**Meaning:** Every privacy protection is on by default. No configuration required.

| Implementation | Where |
|----------------|--------|
| UFW firewall: default deny inbound; outbound restricted as needed. Enabled on first boot. | `config/hooks/live/02-privacy-hardening.hook.chroot`; includes.chroot UFW rules |
| Ghost runs at boot at Level 1 (MAC randomize, hostname, DNS-over-HTTPS, kill switch ready). User is protected without opening an app. | `ghost/ghost.service`; enabled in hook or default target |
| DNS-over-HTTPS (e.g. Quad9) configured by Ghost so ISP cannot see DNS. | Ghost module `dns_config.sh` |
| Kernel-level kill switch (nftables) so if VPN drops, traffic stops. | `config/includes.chroot/etc/nftables.conf`; Ghost `kill_switch.sh` |
| Hardening (sysctl, no core dumps, etc.) applied at build so it is default. | `02-privacy-hardening.hook.chroot` |

**Verification checklist**
- [ ] After first boot, firewall is active and default policy is deny inbound.
- [ ] Ghost service is enabled and runs at boot; Level 1 identity applied.
- [ ] No "opt-in" step required for basic privacy (MAC, hostname, DNS, firewall).

---

## 5. Proven Trust

**Meaning:** Every tool has a track record. No marketing claims — only proven results.

| Implementation | Where |
|----------------|--------|
| Technology choices documented with reason: Debian (stable, reproducible), Mullvad (no-log proven by seizure), KDE (auditable), nftables (kernel-level). | README, `docs/package-rationale.md` |
| Package rationale explains why each list exists; major components have a "why we trust this" note. | `docs/package-rationale.md` |
| No proprietary "trust us" tools for critical path; prefer audited/open components. | Policy in package lists and docs |

**Verification checklist**
- [ ] Each major component (base, VPN, firewall, wipe tool) has a documented rationale or audit link.
- [ ] No inclusion of tools that rely solely on marketing claims for security/privacy.

---

## Summary

| Principle | Build-time / default behavior |
|-----------|-------------------------------|
| **Zero Bloat** | Explicit package lists only; strip unneeded; no hidden extras. |
| **Zero Telemetry** | Strip telemetry packages; disable crash reporters; block telemetry domains in hosts. |
| **AI Training Protection** | Block AI/data-collection domains; no default cloud sync; document guarantee. |
| **Privacy By Default** | Firewall on, Ghost at boot, DoH, kill switch; hardening applied by default. |
| **Proven Trust** | Document rationale for every major tool; prefer proven/audited components. |

*Your machine. Your data. Nobody else's business.*
