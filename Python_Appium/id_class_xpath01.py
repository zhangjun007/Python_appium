#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/10 14:32

from appium import webdriver

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '7.0'
desired_caps["deviceName"] = 'localhost'
desired_caps["appPackage"] = 'com.android.settings'
desired_caps["appActivity"] = 'com.android.settings.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#需求：定位设置的搜索框，输入内容后，点击返回键

# 通过元素id来定位 搜索 按钮，并点击
driver.find_element_by_id("com.android.settings:id/search").click()
time.sleep(5)

#通过class_name 定位 输入框，并点击
driver.find_element_by_class_name("android.widget.EditText").send_keys("Wi-Fi")
time.sleep(5)

#通过 xpath 元素定位 返回键，并点击
driver.find_element_by_xpath("//*[@content-desc='Collapse']").click()


time.sleep(5)

driver.quit()