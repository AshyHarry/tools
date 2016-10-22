# -*- coding: UTF-8 -*-
import os
import re
import urllib.request

import requests
from lxml import etree
from pprint import pprint


class Open163:
    def __init__(self):
        self.course_url = ''
        self.courselist = []
        self.videolist = []
        self.srtlist_en = []
        self.srtlist_cn = []
        self.course = {}

    def set_url(self, course_url):
        self.course_url = course_url

    def get_courselist(self):
        """
        this method get every course url from the url given
        now it can used to get every course in ope..163.com
        :param self:
        :return:
        """

        html_source_list = requests.get(url=self.course_url)
        html = html_source_list.text
        doc = etree.HTML(html)
        # url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
        url_courses = doc.xpath('//*/body/*/div/*/table/*/td/a')
        # url_courses = doc.xpath('/html/body/div[6]/div[0]/table[1]/tbody/a')
        for dummy_url in url_courses:
            if dummy_url.get('href') is not None:
                if dummy_url.get('href') not in self.courselist:
                    self.courselist.append(dummy_url.get('href'))
        return self.courselist

    def get_videolist(self):
        tmp_list = []
        for dummy_index in range(len(self.courselist)):
            detail = requests.get(self.courselist[dummy_index])
            html_detail = detail.text
            doc = etree.HTML(html_detail)
            video_doc = doc.xpath('/html/body/script[14]/text()')
            tmp_list.append(re.findall('http.*?\.m3u8', video_doc[0]))
        for dummy_index in range(len(tmp_list)):
            dummy_list = tmp_list[dummy_index][0].replace('.m3u8', '.mp4')
            self.videolist.append(dummy_list)
        return self.videolist

    def get_srtlist(self):
        dummy_srtlist = []
        for dummy_index in range(len(self.courselist)):
            dummy_srtlist0 = self.courselist[dummy_index].replace('.html', '.xml')
            dummy_srtlist1 = dummy_srtlist0.replace(dummy_srtlist0[-35:-23], dummy_srtlist0[-28:-23] + '2_')
            dummy_srtlist2 = dummy_srtlist1.replace('open.163.com', 'live.ws.126.net')
            dummy_srtlist.append(dummy_srtlist2)
        # '''
        # the method below is using beautiful soup
        # '''
        # for i in range(len(dummy_srtlist)):
        #     url = dummy_srtlist[i]
        #     xml_res = requests.get(url)
        #     xml_doc = xml_res.text
        #     xml_soup = BeautifulSoup(xml_doc, 'lxml')
        #     if xml_soup.subs:
        #         for sub in xml_soup.subs:
        #             if sub:
        #                 for child in sub:
        #                     dummy_srt = sub.url.get_text().encode('utf-8')
        #                     if child.get_text().encode('utf-8') == '中文':
        #                         srtlist_CN.append(dummy_srt)
        #                     elif child.get_text().encode('utf-8') == '英文':
        #                         srtlist_EN.append(dummy_srt)
        #                     else:
        #                         pass
        #             else:
        #                 print ("This course has no caption1!")
        #     else:
        #         print ("This course has no caption2!")

        for dummy_index in range(len(dummy_srtlist)):
            dummy_url = dummy_srtlist[dummy_index]
            xml_res = requests.get(dummy_url)
            xml_doc = xml_res.text.encode('utf-8')
            doc = etree.XML(xml_doc)
            res_url = doc.xpath('/all/subs/sub/url/text()')
            # res_lang = doc.xpath('/all/subs/sub/name/text()')
            try:
                self.srtlist_cn.append(res_url[0])
            except:
                pass
            try:
                self.srtlist_en.append(res_url[1])
            except:
                pass
        return self.srtlist_cn, self.srtlist_en

    def format(self):
        for dummy_index in range(len(self.courselist)):
            self.course['lesson' + str(dummy_index + 1)] = {
                'video': self.videolist[dummy_index],
                'chinese_srt': self.srtlist_cn[dummy_index],
                'english_srt': self.srtlist_en[dummy_index]
            }
        return self.course


def download_srt(download_url, filename):
    dir_here = os.getcwd()
    ori_dir = dir_here + '\document\srt'  # set the dictionary to get original json data
    if not os.path.exists(ori_dir):
        os.makedirs(ori_dir)
    tmp_srt = urllib.request.urlopen(download_url)
    full_filename = ori_dir + '\\' + filename + '.txt'
    with open(full_filename, 'wb') as f:
        f.write(tmp_srt.read())
    dummy_lines = tmp_srt.readlines()
    for li in dummy_lines:
        pprint(li)
    return 0


if __name__ == '__main__':
    url = 'http://open.163.com/special/opencourse/cs50.html'
    # courses = Open163()
    # courses.set_url(url)
    # cou = courses.get_courselist()
    # video = courses.get_videolist()
    # srt_cn, srt_en = courses.get_srtlist()
    # srt = courses.format()
    # pprint(cou)
    # pprint(video)
    # pprint(srt)
    # if len(srt_cn) != 0:
    #     for i in range(len(srt_cn)):
    #         download_srt(srt_cn[i], 'lesson' + str(i) + '_cn')
    # if len(srt_en) != 0:
    #     for i in range(len(srt_en)):
    #         download_srt(srt_en[i], 'lesson' + str(i) + '_en')

    download_srt('http://oc-caption-srt.nos.netease.com/oc-srt-1427263334216.srt', str(1))
