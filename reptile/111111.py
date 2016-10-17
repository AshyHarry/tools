import re
import requests
# import lxml
import beautifulsoup
import beautifulsoup
from sgmllib import SGMLParser
url_source_list = 'http://open.163.com/special/opencourse/cs50.html'
html_source_list = requests.get(url=url_source_list)
doc = lxml.etree.HTML(html_source_list)
result = doc.xpath('//*[@id="list1"]/tbody/tr[2]/td[1]/a')
print result
url = 'http://open.163.com/movie/2010/3/9/K/M6U6LS8CV_M6U6NDE9K.html'
data = requests.get(url=url)
print re.findall('http.*m3u8',data.text),type(data.content)
