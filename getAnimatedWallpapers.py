#!/usr/bin/python
import os
import json
import shutil
import string
import subprocess
from dotenv import load_dotenv
from animatedWallpapers import (
    get_files,
    append_index,
    play_video,
    read_index,
    selected_video,
)

load_dotenv()

STEAM_USER = os.getenv("STEAM_USER")
WALLPAPER_ENGINE = os.getenv("WALLPAPER_ENGINE_ID")
VIDEOS_FOLDER = "/home/bleakness/wallpapers/videos/"

steam_link = subprocess.check_output("wl-paste", shell=True).decode()


def isUrlValid(url):
    return url.startswith("https://steamcommunity.com/")


def getItemId(url):
    return url.split("?id=")[1].split("&")[0]


def getVideoPath(
    ITEM_ID, path="/home/bleakness/wallpapers/steamcmd/steamapps/workshop/content/"
):
    return path + f"{WALLPAPER_ENGINE}/{ITEM_ID}"


def getVideoName(ITEM_ID):
    root = getVideoPath(ITEM_ID) + "/"

    json_file = [file for file in os.listdir(root) if file.endswith(".json")][0]

    with open(root + json_file) as json_data:
        json_file = json.load(json_data)

    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

    wallpaper_name = "".join(c for c in json_file["title"] if c in valid_chars).strip()

    return wallpaper_name


def moveVideo(path, wallpaper_name):
    root = path + "/"
    file = [
        file
        for file in os.listdir(root)
        if file.endswith(".mp4") or file.endswith(".mpv")
    ][0]
    video_extension = "." + file.split(".")[-1]
    video_full_name = root + wallpaper_name + video_extension


    shutil.move(root + file, VIDEOS_FOLDER + f"{wallpaper_name + video_extension}")


    if os.path.exists(
        "/home/bleakness/wallpapers/steamcmd/steamapps/workshop/content/"
    ):
       shutil.rmtree("/home/bleakness/wallpapers/steamcmd/steamapps/workshop/content/")



def downloadVideo(ITEM_ID, path="/home/bleakness/wallpapers/steamcmd/"):
    download_steam_command = f'steamcmd +force_install_dir "{path}" +login {STEAM_USER} +workshop_download_item {WALLPAPER_ENGINE} {ITEM_ID} +quit'
    os.system(download_steam_command)


def run(ITEM_ID):
    if isUrlValid(steam_link):
        downloadVideo(ITEM_ID)
        video_path = getVideoPath(ITEM_ID)
        video_name = getVideoName(ITEM_ID)
        moveVideo(video_path, video_name)

        # Play just downloaded video
        files = get_files()
        for i in range(len(files)):
            if files[i].replace("." + files[i].split(".")[-1], "") == video_name:
                append_index(str(i))
                play_video(selected_video(int(read_index())))
                break


ITEM_ID = getItemId(steam_link)
run(ITEM_ID)
