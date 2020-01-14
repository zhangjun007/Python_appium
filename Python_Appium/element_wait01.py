#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/13 19:19

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

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#隐式等待
driver.implicitly_wait(20)

#重点：隐式等待使用此方法

#隐式等待适用于 全局

print("-----begin find")
element_wait = driver.find_element_by_id("com.tcl.live:id/tv_download")

print("-----begin click")
element_wait.click()


time.sleep(3)

driver.quit()