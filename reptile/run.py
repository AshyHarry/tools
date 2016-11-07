# -*- coding = 'UTF-8' -*-

import os
from pprint import pprint

import requests
from lxml import etree

from reptile.open163_PCweb import Open163, get_srt
from reptile.open163_mobilereq import get_original_data, download_srt, format_srt

# if __name__ == '__main__':
#     pprint(os.path.realpath(__file__))
#     pprint(os.path.dirname(os.path.realpath(__file__)))
#     pprint(os.getcwd())
#
#     video, srt_cn, srt_en = get_original_data()
#     # pprint(srt_cn)
#     # pprint(srt_en)
#     # pprint(video)
#
#     for i in range(len(srt_cn)):
#         download_srt(srt_cn[i], 'lesson' + str(i + 1) + '_cn')
#     for i in range(len(srt_en)):
#         download_srt(srt_en[i], 'lesson' + str(i + 1) + '_en')
#
#     dir_here = os.getcwd()
#     in_dir = dir_here + '\document\srtAPP'
#     # out_dir = dir_here + '\document\document_final'
#     # if not os.path.exists(in_dir):
#     #     print('Please download original srt file frist!')
#     #     exit()
#     # if not os.path.exists(out_dir):
#     #     os.makedirs(out_dir)
#     for parent, dirnames, filenames in os.walk(in_dir):
#         for filename in filenames:
#             in_file = os.path.join(parent, filename)
#             format_srt(in_file)


# if __name__ == '__main__':
#     url = 'http://open.163.com/special/opencourse/cs50.html'
#     html_source_list = requests.get(url=url)
#     html = html_source_list.text
#     doc = etree.HTML(html)
#     # url_courses = doc.xpath('//td/a/@href')
#     url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]//@href')
#     # url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
#     pprint(url_courses)

if __name__ == '__main__':
    url = 'http://open.163.com/special/opencourse/cs50.html'
    courses = Open163()
    courses.set_url(url)
    courselist = courses.get_courselist()
    video = courses.get_videolist()
    srt_cn, srt_en = courses.get_srtlist()
    srt = courses.format()
    # pprint(courselist)
    pprint(video)
    # pprint(srt)
    dummy_srtlist = []
    for dummy_index in range(len(courselist)):
        dummy_srtlist0 = courselist[dummy_index].replace('.html', '.xml')
        dummy_srtlist1 = dummy_srtlist0.replace(dummy_srtlist0[-35:-23], dummy_srtlist0[-28:-23] + '2_')
        dummy_srtlist2 = dummy_srtlist1.replace('open.163.com', 'live.ws.126.net')
        dummy_srtlist.append(dummy_srtlist2)
    pprint(dummy_srtlist)
    srt = []
    for dummy_index in range(len(dummy_srtlist)):
        dummy_url = dummy_srtlist[dummy_index]
        xml_res = requests.get(dummy_url)
        xml_doc = xml_res.text.encode('utf-8')
        doc = etree.XML(xml_doc)
        # res_url = doc.xpath('/all/subs/sub/url/text()')
        res_url = doc.xpath('//sub/url/text()')
        srt.append(res_url)
        # pprint(res_url)
        # print(type(res_url))
    pprint(srt)
    # print(type(srt[0]))