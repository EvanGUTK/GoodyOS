#!/usr/bin/env python3
"""
GoodyOS Ghost — GTK GUI for identity and privacy control.
Shows: current Ghost level, identity status, VPN status, one-click New Identity.
System tray icon shows current level.
"""
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, GLib  # noqa: E402

APP_NAME = "Ghost"
VERSION = "1.0"


def main():
    win = Gtk.Window(title=f"{APP_NAME} — GoodyOS")
    win.set_default_size(400, 300)
    win.connect("destroy", Gtk.main_quit)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
    win.add(box)
    label = Gtk.Label(label=f"GoodyOS {APP_NAME}\nLevel: 1 — Daily Driver\n[New Identity] [Panic]")
    label.set_halign(Gtk.Align.CENTER)
    box.pack_start(label, True, True, 0)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
