#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 15:57

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


#根据属性名 和 属性值 操作元素

element_attribute = driver.find_elements_by_class_name("android.widget.ImageView")

for i in element_attribute:
    print(i.get_attribute("enabled"))
    print(i.get_attribute("clickable"))
    print(i.get_attribute("resourceID"))
    print(i.get_attribute("className"))


time.sleep(3)

driver.quit()