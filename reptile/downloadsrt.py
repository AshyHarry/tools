# -*- coding: UTF-8 -*-
import os
import urllib2
import json


def download_srt():
    dir_here = os.getcwd()
    ori_dir = dir_here + '\document\document_original'
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)
    ori_fp = ori_dir + '\original_data.txt'
    if os.path.exists(ori_dir):
        fp = open(ori_fp, 'r')
        url_json = json.load(fp)
        fp.close()
        video_list = url_json['data']['videoList']
        for i in range(len(video_list)):
            url_srt_cn = video_list[i]['subList'][0]['subUrl']
            url_srt_en = video_list[i]['subList'][1]['subUrl']
            srt_filename_cn = 'lesson' + str(i+1) + '_cn.txt'
            srt_filename_en = 'lesson' + str(i+1) + '_en.txt'
            srt_dirname_cn = ori_dir + '\\' + srt_filename_cn
            srt_dirname_en = ori_dir + '\\' + srt_filename_en
            srt_content_cn = urllib2.urlopen(url_srt_cn)
            srt_content_en = urllib2.urlopen(url_srt_en)
            srt_cn = open(srt_dirname_cn, 'wb')
            srt_cn.write(srt_content_cn.read())
            srt_cn.close()
            print 'The chinese subtitle of  Lesson', i + 1, 'has been successfully saved to document_original/', srt_filename_cn, '!'
            srt_en = open(srt_dirname_en, 'wb')
            srt_en.write(srt_content_en.read())
            srt_en.close()
            print 'The english subtitle of  Lesson', i + 1, 'has been successfully saved to document_original/', srt_filename_en, '!'
    else:
        print 'You should get the original json data by run get_original_data.py first!'


if __name__ == '__main__':
    download_srt()
