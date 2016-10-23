# -*- coding: UTF-8 -*-
import json
import os

import re
import requests


def get_original_data():
    url = 'http://c.open.163.com/mob/M6U6LS8CV/getMoviesForIpad.do'
    original_data = requests.get(url=url)   # get original data from the source url
    json_data = original_data.json()
    videolist = json_data['data']['videoList']
    video_url = []
    srt_cn = []
    srt_en = []
    for i in range(len(videolist)):
        video_url.append(videolist[i]['mp4SdUrlOrign'])
        srt_cn.append(videolist[i]['subList'][0]['subUrl'])
        srt_en.append(videolist[i]['subList'][1]['subUrl'])
    """
    # write original_data to file if needed
    dir_here = os.getcwd()  # get current path
    ori_dir = dir_here + '\document'
    ori_file = ori_dir + '\original_data.txt'
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)    # if the dictionary \document_original do not exsit, then create it
    with open(ori_file, 'wb') as fp:
        try:
            fp.write(original_data.text.encode('utf-8'))
        except:
            fp.write(original_data.text)
    print ('The original json data has been successfully saved to document_original/original_data.txt ','!')
    return 0
    """
    return video_url, srt_cn, srt_en


def download_srt(download_url, filename):
    dir_abs = os.path.realpath(__file__)
    dir_here = os.path.dirname(dir_abs)
    ori_dir = dir_here + '\document\srtAPP'  # set the dictionary to get original json data
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)
    print(filename + ' is doloading...')
    tmp_srt = requests.get(download_url)
    full_filename = ori_dir + '\\' + filename + '.txt'
    with open(full_filename, 'wb') as f:
        f.write(tmp_srt.text.encode('UTF-8'))
    print(filename + 'download complete! ')
    return 0


def format_srt(file):
    fp = open(file, 'r', encoding='UTF-8')
    dummy_lines = fp.readlines()
    fp.close()
    dummy_fp = open(file, 'w', encoding='UTF-8')
    for li in dummy_lines:
        if re.findall('\d\d:.*', li):
            pass
        elif re.findall('[1-90]\d*\n', li):
            pass
        elif re.findall('\[.*?]', li):
            pass
        elif not li.split():
            pass
        elif re.findall('【', li):
            pass
        else:
            dummy_li = li.strip('\n').strip('>>').strip(' ').rstrip('\n')
            if re.findall('\.$', dummy_li) or re.findall('\?$', dummy_li) \
                    or re.findall(';$', dummy_li) or re.findall('!$', dummy_li):
                dummy_fp.write(dummy_li + '\n')
            else:
                dummy_fp.write(dummy_li + ' ')
    dummy_fp.close()
