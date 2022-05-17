##
# This class will move image from a specific
# directory to another directory that user chooses
#
# History:
#   2022-05-14 :  Initial commit
#
from os import path
import os
import pathlib
import shutil
import glob

class Organizer:
    def __init__(self):
        pass

    def mover(self):
        # TODO uncomment when done
        # img_directory = input("Enter the location of your files: ")
        img_directory = "/Users/greggtomas/Downloads"
        jpgCounter = len(glob.glob1(img_directory,"*.JPG"));
        print(jpgCounter)
        for image_file in pathlib.Path(img_directory).glob('*.JPG'):
            print(image_file)
        is_move = input("Do you want to move the jpgs file (Y/N)? ")
        if (is_move == 'Y' or is_move == 'y'):
            img_to_directory = input("Which directory? ")
            is_dir = os.path.isdir(img_to_directory)
            # Directory doesn't exist
            if (not is_dir):
                # create directory and move
                self.__create_dir(img_to_directory)
            # move and rename file
            self.__move_files(img_directory, img_to_directory)
        else:
            pass
            
    def __create_dir(self, directory):
        os.mkdir(directory)
        print("Directory '% s' created" % directory)

    def __move_files(self, from_dir, to_dir):
        # used list comprehension
        files = [i for i in os.listdir(from_dir) if i.endswith("JPG") and path.isfile(path.join(from_dir, i))]
        new_filename = "break"
        number = 0
        for f in files:
            shutil.move(path.join(from_dir,f), path.join(to_dir, new_filename+"-"+str(number)+".jpg"))
            number += 1


organizer = Organizer()
organizer.mover()
