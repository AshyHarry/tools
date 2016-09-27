import json
import os

# devices = os.system('adb devices')
# print devices,type(devices)

devices = os.popen('adb devices')
res = devices.read()
if not res.strip():
    print 'No devices connected!'
else:
    # devicesinfo = os.open('cat /system/build.prop | grep "product"')
    devinfo_file = os.popen('adb shell cat /system/build.prop |find "product"')
    with open(devinfo_file, mode='r', buffering=1) as lines:
        for line in lines:
            devinfo = line.rstrip
    print devinfo,type(devinfo)
    # if devinfo_file:
    #     with open(devinfo_file, buffering=1) as devinfo:
    #         print devinfo
    # print type(devinfo_file)
    # fp = open(devinfo_file,'r')
    # devinfo_text = json.load(fp)
    # print devinfo_text,type(devinfo_text)