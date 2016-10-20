# -*- coding: UTF-8 -*-
import codecs
import json
import os

import chardet
import requests


def get_original_data():
    url = 'http://c.open.163.com/mob/M6U6LS8CV/getMoviesForIpad.do'
    original_data = requests.get(url=url)   # get original data from the source url
    dir_here = os.getcwd()  # get current path
    ori_dir = dir_here + '\document'
    ori_file = ori_dir + '\original_data.txt'
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)    # if the dictionary \document_original do not exsit, then create it
    # chardet.detect("original_data.text")
    with open(ori_file, 'wb') as fp:
        try:
            fp.write(original_data.text.encode('utf-8'))
        except:
            fp.write(original_data.text)
        # json.dump(original_data.json(), fp) #write the original json data to original_data.txt in document_original
    print ('The original json data has been successfully saved to document_original/original_data.txt ','!')
    return 0

if __name__ == '__main__':
    get_original_data()
