#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/13 20:42


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


#显示等待  有异常

print("-----begin find")

#显示等待 调用driver对象，在xx时间内，每间隔xx秒进行寻找某些操作
WebDriverWait(driver,20,2).until(lambda x:x.find_element_by_xpath("//*[@resource-id='com.tcl.live:id/tv_download']"))

#以上示例中 WebDriverWait(driver,x,x)  ， until(lambda x:x.find_element_by_xx("xxx")都是固定格式

#显示等待适合某一特定操作，且适用于局域方法，非全局。

time.sleep(3)

driver.quit()