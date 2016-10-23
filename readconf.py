import configparser
import os


def readconf(sec, option):
    dir_now = os.path.realpath(__file__)
    dir_conf = os.path.dirname(dir_now) + '\conf.conf'
    # dir_now = os.getcwd()
    # while dir_now[-5:] <> 'tools':
    #     dir_now = os.path.dirname(dir_now)
    # dir_conf = dir_now + '\conf.conf'
    conf = configparser.ConfigParser()
    conf.read(dir_conf)
    res_conf = conf.get(sec, option)
    return res_conf


if __name__ == '__main__':
    dir_to_rename = readconf('sec', 'dir_to_rename')
    print(dir_to_rename)
