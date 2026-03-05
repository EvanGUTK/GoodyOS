#!/usr/bin/env bash
# Ghost — DNS-over-HTTPS (Quad9 or similar); ISP cannot see queries (Level 1)

set -e
# Configure systemd-resolved or stub resolver for DoH
# Placeholder: actual config depends on resolvconf vs systemd-resolved
if [ -d /etc/systemd/resolved.conf.d ]; then
  mkdir -p /etc/systemd/resolved.conf.d
  cat > /etc/systemd/resolved.conf.d/goodyos.conf << 'EOF'
[Resolve]
DNS=9.9.9.9#https://dns.quad9.net/dns-query
DNSOverTLS=yes
EOF
  systemctl restart systemd-resolved 2>/dev/null || true
fi
echo "[Ghost] DNS-over-HTTPS configured"
