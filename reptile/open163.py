import re
import requests
from lxml import etree
from bs4 import BeautifulSoup
url_source_list = 'http://open.163.com/special/opencourse/cars.html'
html_source_list = requests.get(url=url_source_list)
html = html_source_list.text
doc = etree.HTML(html)
url_courses = doc.xpath('//*[@id="list2"]//*[@class="u-ctitle"]/a')
url_list = []
dummy_url = []
for url in url_courses:
    ss = url.get("href")
    url_list.append(ss)
    ss1 = ss.replace('.html','.xml')
    ss2 = ss1.replace(ss1[-36:-23],ss1[-28:-23]+'2_')
    ss3 = ss2.replace('open.163.com', 'live.ws.126.net')
    dummy_url.append(ss3)


srt_url = []
for i in range(len(dummy_url)):
    url = dummy_url[i]
    print (url)
    xml_res = requests.get(url)
    xml_doc = xml_res.text
    xml_soup = BeautifulSoup(xml_doc, 'lxml')
    if xml_soup.subs:
        if xml_soup.subs.sub:
            if xml_soup.subs.sub.url:
                dummy_srt_url = xml_soup.subs.sub.url.string
                print (dummy_srt_url)
                srt_url.append(dummy_url)

# print srt_url

video_url = []
for i in range(len(url_list)):
    detail = requests.get(url_list[i])
    html_detail = detail.text
    doc = etree.HTML(html_detail)
    video = doc.xpath('/html/body/script[14]/text()')
    video_url.append(re.findall('http.*?\.m3u8',video[0]))

# print video_url[0]