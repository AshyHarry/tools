# -*- coding: UTF-8 -*-
import os
import urllib2
import json


def download_srt():
    ori_fp = open(r'C:\Users\the__\PycharmProjects\tools\reptile\document_original\original_data.txt', 'r')
    url_json = json.load(ori_fp)
    ori_fp.close()
    video_list = url_json['data']['videoList']
    ori_dir = 'C:\\Users\\the__\\PycharmProjects\\tools\\reptile\\document_original'
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)
    for i in range(len(video_list)):
        url_srt_cn = video_list[i]['subList'][0]['subUrl']
        url_srt_en = video_list[i]['subList'][1]['subUrl']
        srt_filename_cn = 'session' + str(i) + '_cn.txt'
        srt_filename_en = 'session' + str(i) + '_en.txt'
        srt_dirname_cn = ori_dir + '\\' + srt_filename_cn
        srt_dirname_en = ori_dir + '\\' + srt_filename_en
        srt_content_cn = urllib2.urlopen(url_srt_cn)
        srt_content_en = urllib2.urlopen(url_srt_en)

        srt_cn = open(srt_dirname_cn, 'wb')
        srt_cn.write(srt_content_cn.read())
        srt_cn.close()
        print '第', i+1, '课的中文字幕已写入document_original文件夹下的', str(srt_filename_cn),'文件！'
        srt_en = open(srt_dirname_en, 'wb')
        srt_en.write(srt_content_en.read())
        srt_en.close()
        print '第', i+1, '课的英文字幕已写入document_original文件夹下的', str(srt_filename_en), '文件！'

if __name__ == '__main__':
    download_srt()
