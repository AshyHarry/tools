#-*- coding: UTF-8 -*-
import os
import re
import requests
from lxml import etree
from bs4 import BeautifulSoup


def get_courselist(course_url):
    '''
    this method get every course url from the url given
    :param course_url:
    :return:
    '''
    html_source_list = requests.get(url=course_url)
    html = html_source_list.text
    doc = etree.HTML(html)
    url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
    courselist = []
    for dummy_url in url_courses:
        courselist.append(dummy_url.get("href"))
    return courselist

def get_videolist(courselist):
    videolist = []
    tmp_list = []
    for i in range(len(courselist)):
        detail = requests.get(courselist[i])
        html_detail = detail.text
        doc = etree.HTML(html_detail)
        video_doc = doc.xpath('/html/body/script[14]/text()')
        tmp_list.append(re.findall('http.*?\.m3u8', video_doc[0]))
    for i in range(len(tmp_list)):
        videolist.append(tmp_list[i][0].encode('utf-8'))
    return videolist

def get_srtlist(courselist):
    dummy_srtlist = []
    srtlist_CN = []
    srtlist_EN = []
    for i in range(len(courselist)):
        dummy_srtlist0 = courselist[i].replace('.html', '.xml')
        dummy_srtlist1 = dummy_srtlist0.replace(dummy_srtlist0[-35:-23], dummy_srtlist0[-28:-23] + '2_')
        dummy_srtlist2 = dummy_srtlist1.replace('open.163.com', 'live.ws.126.net')
        dummy_srtlist.append(dummy_srtlist2)

    '''
    the method below is using beautiful soup
    '''
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

    '''
    the method below is using lxml
    '''
    for i in range(len(dummy_srtlist)):
        url = dummy_srtlist[i]
        xml_res = requests.get(url)
        xml_doc = xml_res.text.encode('gbk')
        root = etree.fromstring(xml_doc)
        # print etree.ElementTree(root)
        # print [ child.tag for child in root ]
        # print root.tag
        doc = etree.XML(xml_doc)
        # srt = doc.xpath('//*[@class="header"]/sapn')
        # print srt
        # tmp_list.append(re.findall('http.*?\.m3u8', video_doc[0]))
    print root.iter()

    return srtlist_CN,srtlist_EN

# def download_srt(download_url):
#     dir_here = os.getcwd()
#     ori_dir = dir_here + '\document'    #set the dictionary to get original json data
#     for i in range(len(download_url)):
#         url_srt_cn = video_list[i]['subList'][0]['subUrl']
#         url_srt_en = video_list[i]['subList'][1]['subUrl']
#         srt_dirname_cn = download_dir + '\\' + 'lesson' + str(i+1) + '_cn.txt'
#         srt_dirname_en = download_dir + '\\' + 'lesson' + str(i+1) + '_en.txt'
#         srt_content_cn = urllib2.urlopen(url_srt_cn)
#         srt_content_en = urllib2.urlopen(url_srt_en)
#         tmp_file = requests.get(download_url)
#         filename = download_url
#         with
#         srt_cn = open(srt_dirname_cn, 'wb')
#         srt_cn.write(srt_content_cn.read())
#         srt_cn.close()
#         print 'The chinese subtitle of  Lesson', i + 1, 'has been successfully saved to ', srt_dirname_cn, '!'
#         srt_en = open(srt_dirname_en, 'wb')
#         srt_en.write(srt_content_en.read())
#         srt_en.close()
#         print 'The english subtitle of  Lesson', i + 1, 'has been successfully saved to ', srt_dirname_en, '!'
#     return 0

if __name__ == '__main__':
    # url = 'http://open.163.com/special/opencourse/spanish.html'
    # # url = 'http://open.163.com/special/opencourse/cs50.html'
    # course = get_courselist(url)
    # video = get_videolist(course)
    # srt_CN,srt_EN = get_srtlist(course)
    # # print (course)
    # # print (video)
    # # print srt_CN
    # # print srt_EN




    # url = 'http://live.ws.126.net/movie/D/A/2_M95G0M6E6_M95PVJFDA.xml'
    # xml_res = requests.get(url)
    # xml_doc = xml_res.text
    # xml_soup = BeautifulSoup(xml_doc, 'lxml')
    # if xml_soup.subs:
    #     # print xml_soup.subs
    #     # print xml_soup.subs.sub
    #     # print xml_soup.subs.sub.url.string
    #     for child in xml_soup.subs:
    #         for grachild in child:
    #             # print grachild.name
    #             # print grachild.string,type(grachild.string)
    #             print grachild.get_text(),type(grachild.get_text().encode('UTF-8')),child.parent

        #
    url = 'http://live.ws.126.net/movie/E/P/2_M95G0M6E6_M95PVEUEP.xml'
    xml_res = requests.get(url)
    xml_doc = xml_res.text.encode('gbk')
    root = etree.fromstring(xml_doc)
    print root.iter()
    for child in root:
        print child.tag
    print etree.Element('pwtime')