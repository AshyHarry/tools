# -*- coding:UTF-8 -*-
import os


def del_blankline(infile, outfile):
    """ Delete blanklines of infile """
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()
    return 0


dir_here = os.getcwd()
in_dir = dir_here + '\document_original'
out_dir = dir_here + '\document\document_formated'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for parent,dirnames,filenames in os.walk(in_dir):
    for dirname in  dirnames:
        print "parent is:" + parent
        print  "dirname is" + dirname
    for filename in filenames:
        print "parent is:"+ parent
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(parent,filename),type(os.path.join(parent,filename))
        out_file = out_dir+ '\\' + filename + '_fromated'
        print out_file
        del_blankline(os.path.join(parent,filename),out_file)

# if __name__ == "__main__":
#     del_blankline("session1.txt", "new_session1.txt")
