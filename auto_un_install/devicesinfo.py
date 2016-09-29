# -*- coding:UTF-8 -*-
import os

version_sdk = {
    '16'    :   'android4.1',
    '17'    :   'android4.2',
    '18'    :   'android4.3',
    '19'    :   'android4.4',
    '20'    :   'android4.4w',
    '21'    :   'android5.0',
    '22'    :   'android5.1',
    '23'    :   'android6.0',
    '24'    :   'android7.0'
}

def get_devicesinfo():
    devices = os.popen('adb devices')
    res = devices.read()
    if res[26:] == '':
        print 'No devices connected!'
        return 0
    else:
        devinfo_mode = os.popen('adb shell cat /system/build.prop |find "ro.product.mode"')
        devinfo_mtext = devinfo_mode.read().rstrip()[17:]
        devinfo_brand = os.popen('adb shell cat /system/build.prop |find "ro.product.brand"')
        devinfo_btext =  devinfo_brand.read().rstrip()[17:]
        dev_content = os.popen('adb shell getprop | find "ro.build.version.sdk"')
        sdk_version = dev_content.read().rstrip()[-3:-1]
        android_version = version_sdk[sdk_version]
        devicesinfo =  devinfo_btext + ' ' + devinfo_mtext + ', ' + android_version
        return devicesinfo


if __name__ == '__main__':
    print get_devicesinfo()