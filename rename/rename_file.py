import os

import sys

import readconf


def rename_file(in_dir,old_name,new_name):
    for parent, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            new_filename = filename.replace(old_name,new_name)
            os.rename(os.path.join(parent, filename), os.path.join(parent, new_filename))
            print(filename)


def print_filename(in_dir):
    for parent, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            print(filename)
    for parent, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            print(filename[0:(len(filename)-5)])

if __name__ == '__main__':
    in_dir = "E:\LEOSVN\Postto\Postto-iOS\V2.0.2"
    rename_file(in_dir,'2.0','2.0.2')
    print_filename(in_dir)
