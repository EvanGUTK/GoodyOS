# GoodyOS Theming Spec

- **Default:** Dark theme (security/dev aesthetic).
- **Dock:** macOS-style bottom (Latte Dock or KDE panel).
- **Branding:** GoodyOS wallpaper, icons, boot splash, login (SDDM).
- **Konsole:** Clean dark profile pre-configured.
- **Target:** Idle RAM under 800MB on clean boot.

Applied at build time via `config/hooks/live/01-kde-theme.hook.chroot` and files in `includes.chroot/usr/share/wallpapers/goodyos` and `themes/`.
