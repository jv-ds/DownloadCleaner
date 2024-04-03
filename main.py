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
        if file.name.endswith('.mov') or file.name.endswith('.mp4'):
            dest = dl_videos
            shutil.move(file.path, dest)
        if file.name.endswith('.pdf') or file.name.endswith('.docx'):
            if file.name.startswith('CamScanner'):
                dest = dl_scans
                shutil.move(file.path, dest)
            dest = dl_files
            shutil.move(file.path, dest)
        if file.name.endswith('.png') or file.name.endswith('.jpeg'):
            dest = dl_images
            shutil.move(file.path, dest)
        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    move_files()