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
        in_dir = dir_here + '\document\document_formated'
        out_dir = dir_here + '\document\document_final'
        if not os.path.exists(in_dir):
            print('Please download original srt file frist!')
            exit()
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        for parent, dirnames, filenames in os.walk(in_dir):
            for filename in filenames:
                in_file = os.path.join(parent, filename)
                out_file = out_dir + '\\' + filename[:-4] + '_fromated.txt'
                del_time(in_file, out_file)
                print('The subtitle file ' + filename + ' has been successfully saved to ', out_file, '!')
