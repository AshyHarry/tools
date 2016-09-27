# -*- coding: UTF-8 -*-
import json
import os
import requests


def get_original_data():
    url = 'http://c.open.163.com/mob/M6U6LS8CV/getMoviesForIpad.do'
    original_data = requests.get(url=url)
    ori_dir = 'C:\\Users\\the__\\PycharmProjects\\tools\\reptile\\document_original'
    ori_file = ori_dir + '\original_data.txt'
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)
    with open(ori_file, 'wb') as fp:
        json.dump(original_data.json(), fp)
    print 'The original json data has been successfully saved to document_original/original_data.txt ', '!'
    return 0


if __name__ == '__main__':
    get_original_data()
