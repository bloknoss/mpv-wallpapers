#!/usr/bin/python3
import os

WALLPAPER_ENGINE_ICON = "$HOME/dev/mpv-wallpapers/images/wallpaper_engine_logo.png"


def displayNotification(title, body):

    NOTIF_COMMAND = (
        f'notify-send "{title}" "{body}" --expire-time=3000 --icon="{WALLPAPER_ENGINE_ICON}" --app-name="MPVEngine"'
    )
    os.system(NOTIF_COMMAND)
