#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/10 14:14

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

print("-----开始进入后台")

driver.background_app(5)   #模拟HOMW键点击，将应用进入后台5s后，自动返回到前台

print("-----结束进入后台")

driver.quit()