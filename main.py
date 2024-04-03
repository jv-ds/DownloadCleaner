import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

source_dir = "/Users/jeevan/Downloads"
#Destination Files
dl_files = "/Users/jeevan/Downloads/Downloaded Files"
dl_images = "/Users/jeevan/Downloads/Downloaded Images"
dl_scans = "/Users/jeevan/Downloads/Downloaded Scans"
dl_videos = "/Users/jeevan/Downloads/Downloaded Videos"
dl_sounds = "/Users/jeevan/Downloads/Downloaded Sounds"


def move_files():
    for file in os.scandir(source_dir):
        if file.name.endswith('.wav') or file.name.endswith('.mp3'):
            dest = dl_sounds
            shutil.move(file.path, dest)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    move_files()