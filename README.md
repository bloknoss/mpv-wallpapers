# MPV Wallpapers

This repository contains multiple python scripts made to automatically download wallpapers from the Wallpaper Engine Workshop and use them with [MPVPaper](https://github.com/GhostNaN/mpvpaper).  
 For this to work you'll need to have purchased [Wallpaper Engine](https://store.steampowered.com/app/431960/Wallpaper_Engine/) and have [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD) installed.

> It is important to know that this script will only work with Video type wallpapers, not Scenes or any others.

## Development
This repository was developed just so I could bind a key and automatically download and set an animated wallpaper, this means that unless people discover this repository and ask for new features or a GUI, I won't be making them (in the short term)

## Installation
To use this script you'll need to first clone the repository, most of the things it does is basically executing bash commands so you shouldn't have to worry about installing pip dependencies beyond dotenv.
```bash
git clone https://github.com/bloknoss/ConcesioAPI
cd ./ConcesioAPI
```
## Usage
The way it currently is, it doesn't accept links as a parameter, rather, it simply gets the link from your clipboard and parses it, downloads and automatically plays it, so, to use it you only have to copy the link from the Steam Workshop to your clipboard and execute the script.
```bash
python3 getAnimatedWallpapers.py
```
And just like that your wallpaper you copied is now downloaded and running (or should be).

## Issues
I will not implement many new features to this issue or give it a lot of attention, but if you find any issue or come up with any idea that could be nice you can open an issue or contact me.

## Contribution
Feel free to create any pull requests or provide suggestions for the project.