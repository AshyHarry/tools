def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif inside_code >= 65281 and inside_code <= 65374:
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring


def merge_line(infp,outfp):
    ori_text = open(infp).read()
    # all_the_text = strQ2B(ori_text)
    all_the_text = ori_text
    text = ''
    for i in range(len(all_the_text)-1):
        if ord(all_the_text[i]) == 10:
            text += chr(32)
        elif all_the_text[i] == ';' or all_the_text[i] == '.':
            text = text + all_the_text[i] + '\n'
        else:
            text += all_the_text[i]
    f = open(outfp, 'wb')#, 'utf-8')
    f.write(text)
    f.close()
    # for i in range(len(text)-1):
    #     if ord(text[i]) == 0xe2:
    #         print text[i],i,text[(i-10):(i-1)]
    return 0

if __name__ == "__main__":
    merge_line("new_session2-1.txt", "new_session2-2.txt")
