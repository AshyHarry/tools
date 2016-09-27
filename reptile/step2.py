def del_time(infile, outfile):
    """ Delete blanklines of infile """
    import re
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if re.findall('\d\d:\d\d:\d\d,\d\d\d', li):
            pass
        elif re.findall('[1-90]\d*\n', li):
            pass
        else:
            outfp.writelines(li)
    infp.close()
    outfp.close()
    return 0

if __name__ == "__main__":
    del_time("new_session1.txt", "new_session1-1.txt")
