# -*- coding: UTF-8 -*-
import re
import urllib2
import json
import os
import requests


class Caption(object):

    def __init__(self):
        self.dir_here = os.getcwd()  # get current path

    def get_original_data(self,source_url):
        original_data = requests.get(url=source_url)  # et original data from the source url
        ori_dir = self.dir_here + '\document'
        ori_file = ori_dir + '\original_data.txt'
        if not os.path.exists(ori_dir):
            os.makedirs(ori_dir)  # if the dictionary \document_original do not exsit, then create it
        with open(ori_file, 'wb') as fp:
            json.dump(original_data.json(),
                      fp)  # write the original json data to original_data.txt in document_original
        print 'The original json data has been successfully saved to ' + str(ori_file) + '!'
        return 0

    def download_srt(self):
        ori_dir = self.dir_here + '\document'  # set the dictionary to get original json data
        ori_fp = ori_dir + '\original_data.txt'  # get the original data
        download_dir = self.dir_here + '\document\document_original'  # set the dictionary to save the downloaded files
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
                srt_dir_name_cn = download_dir + '\\' + 'lesson' + str(i + 1) + '_cn.txt'
                srt_dir_name_en = download_dir + '\\' + 'lesson' + str(i + 1) + '_en.txt'
                # download the chinese caption from the url_srt_cn
                srt_content_cn = urllib2.urlopen(url_srt_cn)
                # download the english caption from the url_srt_en
                srt_content_en = urllib2.urlopen(url_srt_en)
                srt_cn = open(srt_dir_name_cn, 'wb')
                srt_cn.write(srt_content_cn.read())
                srt_cn.close()
                # print 'The chinese caption of  Lesson', i + 1, 'has been successfully saved to ',srt_dir_name_cn, '!'
                srt_en = open(srt_dir_name_en, 'wb')
                srt_en.write(srt_content_en.read())
                srt_en.close()
                # print 'The english caption of  Lesson', i + 1, 'has been successfully saved to ',srt_dir_name_en, '!'
            return 0

    @staticmethod
    def format_srt(infile, outfile):
        in_fp = open(infile, "r")
        out_fp = open(outfile, "w")
        lines = in_fp.readlines()
        for li in lines:
            if li.split():
                if re.findall('\d\d:.*', li):
                    pass
                elif re.findall('[1-90]\d*\\n', li):
                    pass
                elif re.findall('\[.*?]', li):
                    pass
                else:
                    tmp_dummy_li = li.strip('>>')
                    dummy_li = tmp_dummy_li.strip('\n') + ' '
                    out_fp.writelines(dummy_li)
        in_fp.close()
        out_fp.close()
        return 0


if __name__ == "__main__":
    srt = Caption()
    url = 'http://c.open.163.com/mob/M6U6LS8CV/getMoviesForIpad.do'
    srt.get_original_data(url)
    srt.download_srt()
    in_dir = srt.dir_here + '\document\document_original'
    out_dir = srt.dir_here + '\document\doc_formatted'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for parent, dir_names, file_names in os.walk(in_dir):
        for filename in file_names:
            in_file = os.path.join(parent, filename)
            out_file = out_dir + '\\' + filename[:-4] + '_formatted.txt'
            srt.format_srt(in_file, out_file)
            print 'The subtitle file ' + filename + ' has been successfully saved to ', out_file, '!'
