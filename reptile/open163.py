# -*- coding: UTF-8 -*-
import re
import requests
from lxml import etree


def get_courselist(course_url):
    '''
    this method get every course url from the url given
    now it can used to get every course in ope..163.com
    '''

    html_source_list = requests.get(url=course_url)
    html = html_source_list.text.encode('utf-8')
    doc = etree.HTML(html)
    url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
    # url_courses = doc.xpath('//*[@id="list2"]/a')
    url_courses = doc.xpath('/html/body/div[6]/div[0]/table[1]/tbody/a')
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
    srtlist_cn = []
    srtlist_en = []
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

    for i in range(len(dummy_srtlist)):
        dummy_url = dummy_srtlist[i]
        xml_res = requests.get(dummy_url)
        xml_doc = xml_res.text.encode('utf-8')
        doc = etree.XML(xml_doc)
        res_url = doc.xpath('/all/subs/sub/url/text()')
        # res_lang = doc.xpath('/all/subs/sub/name/text()')
        srtlist_cn.append(res_url[0])
        srtlist_en.append(res_url[1])
    return srtlist_cn, srtlist_en

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
    url = 'http://open.163.com/special/opencourse/cs50.html'
    course = get_courselist(url)
    video = get_videolist(course)
    caption_cn, caption_en = get_srtlist(course)
    print(course)
    print(video)
    print(caption_cn)
    print(caption_en)
