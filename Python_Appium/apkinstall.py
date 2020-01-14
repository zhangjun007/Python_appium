#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/10 13:30


from appium import webdriver

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '7.0'
desired_caps["deviceName"] = '192.168.9.103:5555'
desired_caps["appPackage"] = 'com.android.settings'
desired_caps["appActivity"] = 'com.android.settings.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#判断应用程序是否安装

if driver.is_app_installed("com.tencent.android.qqdownloader"):

#如果安装就卸载
    driver.remove_app("com.tencent.android.qqdownloader")

#如果没安装就按当前路径安装
else:
    driver.install_app("C:\\Users\\jun-z\\Desktop\\MobileAssistant.apk")

#安装完成 sleep 5 秒
time.sleep(5)

driver.close_app()  # 只是退出当前界面，后台进程还在

