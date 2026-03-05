#!/usr/bin/env bash
# GoodyOS — one-click build (wrapper for auto/build)
# Run on Parrot OS or Debian-based host with: sudo ./build.sh

set -e
cd "$(dirname "$0")"
exec ./auto/build
