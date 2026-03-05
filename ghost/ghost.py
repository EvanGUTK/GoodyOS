#!/usr/bin/env python3
"""
GoodyOS Ghost — GTK GUI for identity and privacy levels.
Shows current level, VPN status, one-click New Identity, system tray icon.
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
try:
    gi.require_version("AppIndicator3", "0.1")
    from gi.repository import AppIndicator3
    HAS_APPINDICATOR = True
except (ValueError, ImportError):
    HAS_APPINDICATOR = False
import os
import subprocess
import sys

GHOST_ROOT = os.environ.get("GHOST_ROOT", "/opt/ghost")
LEVEL_FILE = "/var/run/ghost_level"  # or config path


def get_level():
    try:
        with open(LEVEL_FILE) as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1


def set_level(level):
    try:
        with open(LEVEL_FILE, "w") as f:
            f.write(str(level))
        run_ghost(level)
    except PermissionError:
        pass


def run_ghost(level):
    subprocess.Popen([f"{GHOST_ROOT}/ghost.sh", str(level)], env=os.environ)


def new_identity():
    run_ghost(get_level())


def on_panic(btn):
    # Optional: confirm then trigger Scorched Earth
    d = Gtk.MessageDialog(
        transient_for=btn.get_toplevel(),
        flags=0,
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text="Scorched Earth",
    )
    d.format_secondary_text(
        "This will permanently wipe the machine. Only continue in an emergency."
    )
    if d.run() == Gtk.ResponseType.OK:
        os.environ["SCORCHED_EARTH_CONFIRM"] = "yes"
        subprocess.call([f"{GHOST_ROOT}/modules/scorched_earth.sh"])
    d.destroy()


def build_ui():
    win = Gtk.Window(title="GoodyOS Ghost")
    win.set_default_size(400, 280)
    win.connect("destroy", Gtk.main_quit)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
    box.set_margin_top(24)
    box.set_margin_bottom(24)
    box.set_margin_start(24)
    box.set_margin_end(24)
    win.add(box)

    level = get_level()
    label = Gtk.Label(label=f"Ghost Level: {level}")
    label.set_halign(Gtk.Align.CENTER)
    box.pack_start(label, True, True, 0)

    level_btns = Gtk.Box(spacing=6)
    for lvl in (1, 2, 3):
        b = Gtk.Button(label=f"Level {lvl}")
        b.connect("clicked", lambda w, l: set_level(l), lvl)
        level_btns.pack_start(b, True, True, 0)
    box.pack_start(level_btns, True, True, 0)

    new_id_btn = Gtk.Button(label="New Identity")
    new_id_btn.connect("clicked", lambda w: new_identity())
    box.pack_start(new_id_btn, True, True, 0)

    panic_btn = Gtk.Button(label="Scorched Earth (panic)")
    panic_btn.get_style_context().add_class("destructive-action")
    panic_btn.connect("clicked", on_panic)
    box.pack_start(panic_btn, True, True, 0)

    win.show_all()
    return win


def tray_icon():
    if not HAS_APPINDICATOR:
        build_ui()
        return None
    ind = AppIndicator3.Indicator.new(
        "ghost-goodyos",
        "user-available",
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
    )
    ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    ind.set_title("Ghost")
    menu = Gtk.Menu()
    item = Gtk.MenuItem(label=f"Level {get_level()}")
    menu.append(item)
    show_win = Gtk.MenuItem(label="Show Ghost")
    show_win.connect("activate", lambda w: build_ui())
    menu.append(show_win)
    menu.show_all()
    ind.set_menu(menu)
    return ind


def main():
    if "--tray" in sys.argv:
        tray_icon()
        Gtk.main()
    else:
        build_ui()
        Gtk.main()


if __name__ == "__main__":
    main()
