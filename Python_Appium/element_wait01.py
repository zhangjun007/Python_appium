#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/13 19:19

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '8.1.0'
desired_caps["deviceName"] = 'localhost'
desired_caps["appPackage"] = 'com.tcl.live'
desired_caps["appActivity"] = 'com.tcl.live.activity.MainActivity'
desired_caps['UDID'] = 'P7CAVSQGJ7EYMJB6'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#隐式等待方法
#隐式等待适用于全局
driver.implicitly_wait(20)

#间隔10s再进入Tools界面，验证隐式等待的时间
time.sleep(10)
driver.find_element_by_android_uiautomator('new UiSelector().text("TOOLS")').click()

#进入之后才进行后续操作
print("-----begin find")
element_wait = driver.find_element_by_id("com.tcl.live:id/tv_update_more")
print("-----begin click")
element_wait.click()

time.sleep(3)

driver.quit()