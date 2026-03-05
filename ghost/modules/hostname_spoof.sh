#!/usr/bin/env bash
# Ghost — random hostname on boot (Level 1)

set -e
# Generate random hostname (e.g. goody-xxxx)
HOST="goody-$(od -An -N2 -tx1 /dev/urandom | tr -d ' \n')"
echo "$HOST" > /etc/hostname
hostname "$HOST"
# Update /etc/hosts 127.0.1.1
sed -i "s/127.0.1.1.*/127.0.1.1\t$HOST/" /etc/hosts 2>/dev/null || true
echo "[Ghost] Hostname set to $HOST"
