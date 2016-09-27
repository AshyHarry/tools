# -*- coding: utf-8 -*-


package_name = 'com.leo.basesecret'
apk_dir_path = r'\\192.168.1.200\out\xbase\debug\1.6.0' # 开发包
# apk_dir_path = r'\\192.168.1.200\out\secret_space_proguard' # 混淆包

story_names = {
    'HIDE-581': '举报Base--杨月峰',
    'HIDE-571': '自动push--张衡',
    'HIDE-570': '广告SDK--涂豹',
    'HIDE-569': '官方私信--张衡',
    'HIDE-568': '优化--张衡',
    'HIDE-567': '其他--杨月峰',
    'HIDE-566': 'base内容详情页--杨月峰',
    'HIDE-565': 'Base详情页--杨月峰',
    'HIDE-564': '锁的逻辑--黎文学',
    'HIDE-563': 'Album--黎文学',
    'HIDE-562': '他人account--黎文学',
    'HIDE-561': 'MYBase--杨月峰',
    'HIDE-560': '私信--张衡',
    'HIDE-559': 'Message--张衡',
}

devices = {
    "Sony D6503": "Android 6.0 -- 1080*1920",
    "Samsung note5": "Android 6.0 -- 1440*2560",
}


def get_newest_apk(apk_dir_path):
    import os
    apk_list = sorted(os.listdir(apk_dir_path))
    for apk in apk_list:
        if apk[-3:] not in ['apk']:
            apk_list.remove(apk)
    newest_apk_name = apk_list[len(apk_list) - 1]
    newest_apk_path = apk_dir_path + '\\' + newest_apk_name
    return newest_apk_path


def format_current_time():
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def reinstall(apk_path, package_name):
    import os
    try:
        print(u'正在卸载旧安装包，请稍候...')
        os.system('adb uninstall ' + package_name)
    except:
        print(u'旧安装包卸载过程出错，可能之前已卸载')
    print(u'正在安装最新安装包，请稍候...:')
    print(apk_path)
    os.system('adb install ' + '"' + apk_path + '"' + ' > install.tmp')
    print(u'Congratulations!! 新安装包安装成功')
    log_file = package_name.split('.')[-1:][0] + '.log'
    product_name = get_product_name()
    with open(log_file, 'a') as f:
        f.write("".join([format_current_time(), ' ', apk_path, ' ', product_name, '']))


def get_product_name():
    import os
    os.system('adb devices > device.tmp')
    with open('device.tmp', 'r') as f:
        device_info = f.readlines()
    if os.path.exists('install.tmp'):
        os.remove('install.tmp')
    if os.path.exists('device.tmp'):
        os.remove('device.tmp')
    return device_info[1].replace('device', '')


def generate_devices(newest_apk_path, story_names, devices):
    import os
    file_name = r"D:\devices.txt"
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for story_name in story_names:
            f.write("".join(["【", story_name, "】: ", story_names[story_name], '\n']))
        f.write('\n')
        for device in devices:
            f.write("".join(['手机信息: ', device, " -- ", devices[device], '\n']))
        f.write('\n')
        f.write("".join(["安装包: ", newest_apk_path, '\n' * 2]))
        f.write("".join(['用 "', newest_apk_path, '" 进行验证，此问题已解决', '\n' * 2]))
        f.write("".join(['用 "', newest_apk_path, '" 进行验证，此问题并未解决，故将其Reopen，请开发重修', '\n' * 2]))
    os.system("D:\devices.txt")
    return 0


if __name__ == '__main__':
    apk_path = get_newest_apk(apk_dir_path) # 使用最新包时
    # apk_path = r"\\192.168.1.200\out\secret_space_proguard\secret-share_v1.5.0_2016_09_02_14_11_36_proguard.apk" # 使用特定包时
    reinstall(apk_path, package_name)
    generate_devices(apk_path, story_names, devices)