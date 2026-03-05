#!/usr/bin/env python3
"""
GoodyOS USB Dead Man's Switch.
Polls for registered USB drive every 2–3 seconds.
If Level 3 is armed and USB is removed → trigger Scorched Earth immediately.
If Level 1 or 2 → notification only.
"""

import os
import time
import subprocess
import sys

# Config: path to file that marks the registered USB (e.g. /media/ghost-usb/.goodyos-registered)
USB_MARKER = os.environ.get("GHOST_USB_MARKER", "/media/ghost-usb/.goodyos-registered")
POLL_INTERVAL = 2.5
GHOST_ROOT = os.environ.get("GHOST_ROOT", "/opt/ghost")
LEVEL_FILE = "/var/run/ghost_level"


def get_level():
    try:
        with open(LEVEL_FILE) as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1


def usb_present():
    return os.path.isfile(USB_MARKER)


def trigger_scorched_earth():
    env = os.environ.copy()
    env["SCORCHED_EARTH_CONFIRM"] = "yes"
    subprocess.call([f"{GHOST_ROOT}/modules/scorched_earth.sh"], env=env)


def notify_only():
    subprocess.Popen(["notify-send", "GoodyOS", "USB dead man's switch drive removed (Level 1/2 — no wipe)."])


def main():
    last_seen = usb_present()
    while True:
        time.sleep(POLL_INTERVAL)
        now = usb_present()
        if last_seen and not now:
            level = get_level()
            if level >= 3:
                trigger_scorched_earth()
                sys.exit(0)
            else:
                notify_only()
        last_seen = now


if __name__ == "__main__":
    main()
