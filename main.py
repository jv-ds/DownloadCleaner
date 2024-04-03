import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

source_dir = "/Users/jeevan/Downloads"

#Print filenames for files in Downloads folder
def print_filenames(folder):
    for file in folder:
        print(file.name)


print_filenames(os.scandir(source_dir))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir       # to track Downloads folder
    logging.info(f'start watching directory {path!r}')
    event_handler = LoggingEventHandler()       #should change to function later
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()