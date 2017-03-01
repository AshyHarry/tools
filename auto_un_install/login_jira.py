# import requests
#
#
import requests


def login():
    url = 'http://jira.leoers.com/rest/gadget/1.0/login'
#     s = requests.Session()
#     print type(s)
#     s.get(url)
#     r = s.get('http://jira.leoers.com/cookies')
#     print(r.text)
    headers = {
        'X-Requested-With'  : 'XMLHttpRequest',
        'User-Agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Content-Type'      : 'application/x-www-form-urlencoded',
        'Accept-Encoding'   : 'gzip, deflate',
        'Accept-Language'   : 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie'            : {
            'JSESSIONID'    :   '2B5CB9916A7F9309AE2789A12C4EBAF8',
            'ASESSIONID'    :   '61og0w'
        }
    }

    userdata = {
        'os_username':'shiyanyan',
        'os_password':'shiyanyan',

    }
#
    session = requests.post(url=url,headers=headers,json=userdata)
    return 0
#
#
if __name__=='__main__':
    session = login()
    url = 'http://jira.leoers.com/rest/gadget/1.0/login'
    session = requests.session()
    res = session.get(url)
#     cx = u'/ [\u0000\u00ad\u0600 -\u0604\u070f\u17b4\u17b5\u200c -\u200f\u2028 -\u202f\u2060 -\u206f\ufeff\ufff0 -\uffff] / g'
#     escapable = u'/ [\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g'
#     print cx,escapable
# import os
#
# dir_now = os.getcwd()
# print(dir_now)