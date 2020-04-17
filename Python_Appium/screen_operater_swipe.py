#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 16:42

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '8.1.0'
desired_caps["deviceName"] = 'localhost'
desired_caps["appPackage"] = 'com.tcl.live'
desired_caps["appActivity"] = 'com.tcl.live.activity.MainActivity'
desired_caps['UDID'] = 'd424d295'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

# 屏幕操作一共有三种方法 swipe / scroll / drag_and_drop

# swipe 方法

driver.swipe(200,1300,200,800)   #直接传入坐标值即可

#driver.swipe() 方法的扩展,实现AC应用的连续左滑/右滑/下滑/上滑

windows_size=driver.get_window_size()
print(windows_size)

x=driver.get_window_size()["width"]
y=driver.get_window_size()["height"]
print(x,y)

# 左滑屏
count = 0
while True:
    driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 500)
    time.sleep(3)
    print("这是左滑第%s次"%count)
    count=count+1;
    if count > 2:
        break
print("-------------左滑屏结束----------------")

#右滑屏
count = 0
while True:
    driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 500)
    time.sleep(3)
    print("这是右滑第%s次"%count)
    count=count+1;
    if count > 2:
        break

print("-------------右滑屏结束----------------")

#上滑屏
count = 0
while True:
    driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/7*y)
    time.sleep(1)
    print("这是上滑第%s次"%count)
    count=count+1;
    if count > 10:
        break

print("-------------上滑屏结束----------------")

#下滑屏
count = 0
while True:
    driver.swipe(1/2*x, 1/7*y, 1/2*x, 6/7*y)
    time.sleep(1)
    print("这是下滑第%s次"%count)
    count=count+1;
    if count > 10:
        break

print("----------下滑屏结束，程序运行结束---------------")



time.sleep(3)

driver.quit()

