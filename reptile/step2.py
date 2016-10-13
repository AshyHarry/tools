import os


def del_time(infile, outfile):
    """ Delete blanklines of infile """
    import re
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if re.findall('\d\d:.*', li):
            pass
        elif re.findall('[1-90]\d*\n', li):
            pass
        else:
            outfp.writelines(li)
    infp.close()
    outfp.close()
    return 0

if __name__ == "__main__":
    if __name__ == "__main__":
        dir_here = os.getcwd()
        in_dir = dir_here + '\document\document_formatted'
        out_dir = dir_here + '\document\document_final'
        if not os.path.exists(in_dir):
            print 'Please download original srt file first !'
            exit()
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        for parent, dir_names, file_names in os.walk(in_dir):
            for filename in file_names:
                in_file = os.path.join(parent, filename)
                out_file = out_dir + '\\' + filename[:-4] + '_formatted.txt'
                del_time(in_file, out_file)
                print 'The caption file ' + filename + ' has been successfully saved to ', out_file, '!'
