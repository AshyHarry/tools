import os

import sys

import readconf


def rename_file(in_dir,old_name,new_name):
    for parent, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            new_filename = filename.replace(old_name,new_name)
            os.rename(os.path.join(parent, filename), os.path.join(parent, new_filename))
            print filename


if __name__ == '__main__':
    in_dir = readconf.readconf('sec','dir_to_rename')
    rename_file(in_dir,'1.6.2','1.6.2')
