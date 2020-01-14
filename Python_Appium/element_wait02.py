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
wait = WebDriverWait(driver,20,2)  #显示等待调用此方法

wait.until(lambda x:x.find_element_by_xpath("//*[@resource-id='com.tcl.live:id/tv_download']"))

button.click

time.sleep(3)

driver.quit()