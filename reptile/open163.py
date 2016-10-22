# -*- coding: UTF-8 -*-
import re
import requests
from lxml import etree
from pprint import pprint


def get_courselist(course_url):
    """
    this method get every course url from the url given
    now it can used to get every course in ope..163.com
    :param course_url:
    :return:
    """

    html_source_list = requests.get(url=course_url)
    html = html_source_list.text
    doc = etree.HTML(html)
    # url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
    url_courses = doc.xpath('//*/body/*/div/*/table/*/td/a')
    # url_courses = doc.xpath('/html/body/div[6]/div[0]/table[1]/tbody/a')
    courselist = []
    for dummy_url in url_courses:
        if dummy_url.get('href') is not None:
            if dummy_url.get('href') not in courselist:
                courselist.append(dummy_url.get('href'))
    return courselist


def get_videolist(courselist):
    videolist = []
    tmp_list = []
    for dummy_index in range(len(courselist)):
        detail = requests.get(courselist[dummy_index])
        html_detail = detail.text
        doc = etree.HTML(html_detail)
        video_doc = doc.xpath('/html/body/script[14]/text()')
        tmp_list.append(re.findall('http.*?\.m3u8', video_doc[0]))
    for dummy_index in range(len(tmp_list)):
        dummy_list = tmp_list[dummy_index][0].replace('.m3u8', '.mp4')
        videolist.append(dummy_list)
    return videolist


def get_srtlist(courselist):
    dummy_srtlist = []
    srtlist_cn = []
    srtlist_en = []
    for dummy_index in range(len(courselist)):
        dummy_srtlist0 = courselist[dummy_index].replace('.html', '.xml')
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

    for dummy_index in range(len(dummy_srtlist)):
        dummy_url = dummy_srtlist[dummy_index]
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
    course_list = get_courselist(url)
    video = get_videolist(course_list)
    caption_cn, caption_en = get_srtlist(course_list)
    course = {}
    for i in range(len(course_list)):
        course['lesson' + str(i + 1)] = {
            'video': video[i],
            'chinese caption': caption_cn[i],
            'english caption': caption_en[i]
        }
    pprint(course_list)
    # pprint(video)
    # pprint(caption_cn)
    # pprint(caption_en)
    # pprint(course)
    # print(type(course))
    # print(type(course[0]))
    pp = course['lesson16']['video']
    print(pp)
    print(course['lesson3']['chinese caption'])
