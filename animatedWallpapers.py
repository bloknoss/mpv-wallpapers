#!/usr/bin/python
from notificationService import displayNotification
import sys
import subprocess
import os


VIDEOS_FOLDER = "/home/alvaro/wallpapers/videos/"
INDEX_FILE = VIDEOS_FOLDER + "index"


def isMPVRunning():
    run = subprocess.run(
        "ps aux | awk '{print $11'} | grep 'mpvpaper'", shell=True, text=False
    )
    if run.returncode == 0:
        return True
    return False


def play_video(VIDEO_NAME):
    set_wallpaper_command = ""

    RUNNING = isMPVRunning()
    if RUNNING == True:
        set_wallpaper_command = f"echo 'loadfile \"{VIDEOS_FOLDER + VIDEO_NAME}\"' | socat - /tmp/mpv-socket&"
    else:
        set_wallpaper_command = f'mpvpaper -o "no-audio --loop-playlist input-ipc-server=/tmp/mpv-socket" "*" "{VIDEOS_FOLDER + VIDEO_NAME}"&'

    displayNotification(
        "MPV Engine", f"Wallpaper {VIDEO_NAME.split('.')[:-1]} now playing"
    )
    os.system(set_wallpaper_command)


def append_index(index):
    with open(INDEX_FILE, "w") as INDEX:
        INDEX.write(str(index))


def read_index():
    with open(INDEX_FILE, "r") as INDEX:
        return INDEX.read()


def get_files():
    return [
        file for file in os.listdir(VIDEOS_FOLDER) if file.endswith(".mp4" or ".mpv")
    ]


def get_files_count():
    return len(get_files())


def selected_video(index):
    return get_files()[index]


if not os.path.isfile(INDEX_FILE):
    append_index("0")
