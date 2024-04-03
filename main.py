import os

source_dir = "/Users/jeevan/Downloads"

#Print filenames for files in Downloads folder
def print_filenames(folder):
    for file in folder:
        print(file.name)


print_filenames(os.scandir(source_dir))