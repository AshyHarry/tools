# -*-coding='UTF-8'-*-
import webbrowser
from pprint import pprint
from lxml import etree
import requests


# url = 'https://loreal.tmall.com/category.htm?spm=a1z10.1-b-s.w5001-14989537912.4.g35xOT&search=y&scene=taobao_shop'
# page = requests.get(url)
# doc = etree.HTML(page.text)
# res = doc.xpath('//*[@class="detail"]//a/text()')
# pprint(res)

url = 'https://loreal.tmall.com/category.htm?spm=a1z10.1-b-s.w5001-14989537912.4.g35xOT&search=y&scene=taobao_shop'
page = webbrowser.open(url)
print(type(page))
print(page)