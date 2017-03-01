# -*- coding: utf-8 -*-
import os
from readconf import readconf


def get_devicesinfo():
    version_sdk = {
        '16': 'android4.1',
        '17': 'android4.2',
        '18': 'android4.3',
        '19': 'android4.4',
        '20': 'android4.4w',
        '21': 'android5.0',
        '22': 'android5.1',
        '23': 'android6.0',
        '24': 'android7.0'
    }
    devices = os.popen('adb devices')
    res = devices.read()
    if res[26:] == '':
        return 0
    else:
        devinfo_mode = os.popen('adb shell cat /system/build.prop |find "ro.product.mode"')
        devinfo_mtext = devinfo_mode.read().rstrip()[17:]
        devinfo_brand = os.popen('adb shell cat /system/build.prop |find "ro.product.brand"')
        devinfo_btext = devinfo_brand.read().rstrip()[17:]
        dev_content = os.popen('adb shell getprop | find "ro.build.version.sdk"')
        sdk_version = dev_content.read().rstrip()[-3:-1]
        android_version = version_sdk[sdk_version]
        devicesinfo = devinfo_btext + ' ' + devinfo_mtext + ', ' + android_version
        return devicesinfo


def get_newest_apk(apk_dir):
    apk_list = sorted(os.listdir(apk_dir))
    for apk in apk_list:
        if apk[-3:] not in ['apk']:
            apk_list.remove(apk)
    newest_apk_name = apk_list[len(apk_list) - 1]
    newest_apk_path = apk_dir + os.sep + newest_apk_name
    # newest_apk = apk_dir + '\\' + newest_apk_name
    return newest_apk_path


def format_current_time():
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def reinstall(apk_dir, package_name, devices):
    apk_list = sorted(os.listdir(apk_dir))
    for apk in apk_list:
        if apk[-3:] not in ['apk']:
            apk_list.remove(apk)
    newest_apk_name = apk_list[len(apk_list) - 1]
    newest_apk = apk_dir + '\\' + newest_apk_name
    if not devices:
        print('No devices connected!')
    else:
        try:
            print(u'正在卸载旧安装包，请稍候...')
            os.system('adb uninstall ' + package_name)
        except:
            print(u'旧安装包卸载过程出错，可能之前已卸载')
        print(u'正在安装最新安装包，请稍候...:')
        os.system('adb install ' + '"' + apk_dir)
        # os.system('adb install ' + package_name)
        print(newest_apk)
        print(u'Congratulations!! 新安装包安装成功')
        log_file = 'log.log'
        product_name = devices+'\n'
        with open(log_file, 'a') as f:
            f.write(''.join([format_current_time(), ' ', newest_apk, ' was installed to ', product_name]))
    return 0


def generate_devices(newest_apk_path, story_names, devices):
    if not devices:
        return 0
    else:
        dir_now = os.getcwd()
        file_name = dir_now + '\log.txt'
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'w') as f:
            for story_name in story_names:
                f.write(''.join(['【', story_name, '】: ', story_names[story_name], '\n']))
            f.write(''.join(['手机信息',devices]))
            f.write('\n')
            f.write(''.join(['安装包: ', newest_apk_path]))
            f.close()
        return 0


if __name__ == '__main__':
    package_name = readconf('sec', 'package_name')
    apk_dir = readconf('sec', 'apk_dir')
    devices = get_devicesinfo()
    reinstall(apk_dir, package_name, devices)
    generate_devices(apk_dir, '', devices)
