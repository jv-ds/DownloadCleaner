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

#Extension names
image_names = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_names = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
sound_names = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
doc_names = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def move_files():
    for file in os.scandir(source_dir):
        if file.name.endswith(tuple(sound_names)):
            dest = dl_sounds
            shutil.move(file.path, dest)
        elif file.name.endswith(tuple(video_names)):
            dest = dl_videos
            shutil.move(file.path, dest)
        elif file.name.endswith(tuple(doc_names)):
            if file.name.startswith('CamScanner'):
                dest = dl_scans
                shutil.move(file.path, dest)
            dest = dl_files
            shutil.move(file.path, dest)
        elif file.name.endswith(tuple(image_names)):
            dest = dl_images
            shutil.move(file.path, dest)
        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    move_files()