def fromatreg():
    import re
    fp = open("Required_Python_Knowledge.txt")
    fp_text = fp.read()
    fp.close()
    # fp_line = fp.readlines()
    text = ''
    for i in range(len(fp_text)-1):
        if ord(fp_text[i]) == 10:
            text += '\\'
        else:
            text += fp_text[i]

    # for dummy_line in fp_line:
    #     if re.findall('\\n',dummy_line):
    #         text +=
    text_list = text.split()
    for index, word in enumerate(text_list):
        word = word.lower()
        if re.findall('\\c.*', word):
            text_list[index] = '{' + word
        if re.findall('\|\}',word):
            text_list[index] = word + '}'
    fp_text = ' '.join(text_list)
    with open("Required_Python_Knowledge.txt",'wb') as fp:
        fp.write(fp_text)
    print text_list
    return 0


if __name__ == '__main__':
    fromatreg()
