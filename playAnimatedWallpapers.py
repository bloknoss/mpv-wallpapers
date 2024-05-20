#!/usr/bin/python
import sys
import os
from notificationService import displayNotification
from animatedWallpapers import (
    get_files_count,
    read_index,
    append_index,
    play_video,
    selected_video,
)

if __name__ == "__main__":
    SELECTED_INSTRUCTION = sys.argv[1]

    if SELECTED_INSTRUCTION == "f" or SELECTED_INSTRUCTION == "forwards":
        current_index = int(read_index())
        if current_index == get_files_count() - 1:
            append_index(0)
        else:
            append_index(int(current_index + 1))

    elif SELECTED_INSTRUCTION == "b" or SELECTED_INSTRUCTION == "backwards":
        current_index = int(read_index())
        if current_index == 0:
            append_index(get_files_count() - 1)
        else:
            append_index(int(current_index - 1))

    elif SELECTED_INSTRUCTION == "p" or SELECTED_INSTRUCTION == "backwards":
        TOGGLE_STATE_COMMAND = "echo 'cycle pause' | socat - /tmp/mpv-socket"
        os.system(TOGGLE_STATE_COMMAND)

    play_video(selected_video(int(read_index())))
