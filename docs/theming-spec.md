# GoodyOS Theming Spec

- **Default:** dark theme (security/dev aesthetic).
- **Dock:** macOS-style bottom (Latte Dock or KDE panel).
- **Branding:** GoodyOS wallpaper, icons, boot splash, login (SDDM).
- **Konsole:** clean dark profile.
- **Target:** idle RAM under 800 MB on clean boot.

Applied at build time via `config/hooks/live/01-kde-theme.hook.chroot`. Assets in `config/includes.chroot/usr/share/wallpapers` and `themes`. Branding assets in `branding/`.
