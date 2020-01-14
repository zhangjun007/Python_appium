#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 16:42

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '7.0'
desired_caps["deviceName"] = 'localhost'
desired_caps["appPackage"] = 'com.tcl.live'
desired_caps["appActivity"] = '.activity.MainActivity t55'
desired_caps['UDID'] = 'SSDA5L5SQWV8HEHU'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#隐式等待
driver.implicitly_wait(20)


# 屏幕操作一共有三种方法 swipe / scroll / drag_and_drop

# swipe 方法