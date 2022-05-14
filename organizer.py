##
# This class will move image from a specific
# directory to another directory that user chooses
#
# History:
#   2022-05-14 :  Initial commit
#
import os
import pathlib

class Organizer:
    def __init__(self):
        pass

    def mover(self):
        # TODO uncomment when done
        # img_directory = input("Enter the location of your files: ")
        img_directory = "/Users/greggtomas/Downloads"
        for image_file in pathlib.Path(img_directory).glob('*.JPG'):
            print(image_file)
        is_move = input("Do you want to move the file (Y/N)? ")
        if (is_move == 'Y' or is_move == 'y'):
            img_to_directory = input("Which directory? ")
            is_dir = os.path.isdir(img_to_directory)
            # Directory exist?
            if (is_dir):
                # move and rename file
                print(is_dir)
            else:    
                # create directory and move
                self.__create_dir(img_to_directory)        
            
        else:
            pass
            
    def __create_dir(self, directory):
        os.mkdir(directory)
        print("Directory '% s' created" % directory)



organizer = Organizer()
organizer.mover()
organizer.__create_dir("/Users/greggtomas/Documents/test")