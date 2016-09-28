# -*- coding: UTF-8 -*-
import os
import urllib2
import json


def download_srt():
    dir_here = os.getcwd()
    ori_dir = dir_here + '\document'    #set the dictionary to get original json data
    ori_fp = ori_dir + '\original_data.txt' #get the original data
    download_dir = dir_here + '\document\document_original' #set the dictionary to save the downloaded files
    if not os.path.exists(ori_fp):
        print 'You should get the original json data by run get_original_data.py first!'
        return 0
    else:
        if not os.path.exists(download_dir):
                os.makedirs(download_dir)
        fp = open(ori_fp, 'r')
        url_json = json.load(fp)
        fp.close()
        video_list = url_json['data']['videoList']
        for i in range(len(video_list)):
            url_srt_cn = video_list[i]['subList'][0]['subUrl']
            url_srt_en = video_list[i]['subList'][1]['subUrl']
            srt_dirname_cn = download_dir + '\\' + 'lesson' + str(i+1) + '_cn.txt'
            srt_dirname_en = download_dir + '\\' + 'lesson' + str(i+1) + '_en.txt'
            srt_content_cn = urllib2.urlopen(url_srt_cn)
            srt_content_en = urllib2.urlopen(url_srt_en)
            srt_cn = open(srt_dirname_cn, 'wb')
            srt_cn.write(srt_content_cn.read())
            srt_cn.close()
            print 'The chinese subtitle of  Lesson', i + 1, 'has been successfully saved to ', srt_dirname_cn, '!'
            srt_en = open(srt_dirname_en, 'wb')
            srt_en.write(srt_content_en.read())
            srt_en.close()
            print 'The english subtitle of  Lesson', i + 1, 'has been successfully saved to ', srt_dirname_en, '!'
        return 0

if __name__ == '__main__':
    download_srt()
