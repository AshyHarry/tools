import urllib2
import json

def download():
    fp = open('orginaldata.txt','r')
    url_json = json.load(fp)
    url_srt_cn = url_json['data']['videoList'][2]['subList'][0]['subUrl']
    url_srt_en = url_json['data']['videoList'][2]['subList'][1]['subUrl']
    # url_srt_cn = url_json['data']['videoList'][3]['subList'][0]['subUrl']
    # url_srt_en = url_json['data']['videoList'][3]['subList'][1]['subUrl']
    print url_srt_cn,url_srt_en
    f = urllib2.urlopen(url_srt_en)
    srt_name = 'harry_en.srt'
    with open(srt_name, "wb") as srt_cn:
        srt_cn.write(f.read())


if __name__ == '__main__':
    download()