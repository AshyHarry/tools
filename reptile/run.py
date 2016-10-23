# -*- coding = 'UTF-8' -*-

import os
from pprint import pprint

from reptile.open163_mobilereq import get_original_data, download_srt, format_srt

if __name__ == '__main__':
    pprint(os.path.realpath(__file__))
    pprint(os.path.dirname(os.path.realpath(__file__)))
    pprint(os.getcwd())

    video, srt_cn, srt_en = get_original_data()
    # pprint(srt_cn)
    # pprint(srt_en)
    # pprint(video)

    for i in range(len(srt_cn)):
        download_srt(srt_cn[i], 'lesson' + str(i + 1) + '_cn')
    for i in range(len(srt_en)):
        download_srt(srt_en[i], 'lesson' + str(i + 1) + '_en')

    dir_here = os.getcwd()
    in_dir = dir_here + '\document\srtAPP'
    # out_dir = dir_here + '\document\document_final'
    # if not os.path.exists(in_dir):
    #     print('Please download original srt file frist!')
    #     exit()
    # if not os.path.exists(out_dir):
    #     os.makedirs(out_dir)
    for parent, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            in_file = os.path.join(parent, filename)
            format_srt(in_file)
