#!/usr/bin/env bash
# GoodyOS — one-click build (sync Ghost into image, then live-build)
# Run on Debian/Parrot host: ./build.sh   (sudo for lb build)

set -e
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

echo "[GoodyOS] Syncing Ghost app into includes.chroot..."
mkdir -p config/includes.chroot/opt/ghost
rsync -a --exclude='.git' ghost/ config/includes.chroot/opt/ghost/ 2>/dev/null || {
  cp -r ghost/* config/includes.chroot/opt/ghost/
}
chmod +x config/includes.chroot/opt/ghost/ghost.sh
chmod +x config/includes.chroot/opt/ghost/modules/*.sh 2>/dev/null || true

echo "[GoodyOS] Running live-build..."
if [ -n "$1" ] && [ "$1" = "clean" ]; then
  sudo lb clean
fi
sudo lb build

echo "[GoodyOS] Done. ISO: live-image-amd64.hybrid.iso → goodyos.iso"
cp -n live-image-amd64.hybrid.iso goodyos.iso 2>/dev/null || true
