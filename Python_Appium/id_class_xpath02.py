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

#需求：通过id / class——name / xpath的方式获取一组内容元素

# 通过元素id来定位当前页面 resource-id 为 android:id/title 的内容；
id_all = driver.find_elements_by_id("android:id/title")
print(id_all)
print(len(id_all))
for title in id_all:
    print(title.text)

id_all[2].click()   #取元素组里面的任意值进行取值并操作

time.sleep(5)
#
# # 通过 class-name 来定位当前页面元素 class 为 android.widget.TextView 的内容；
classall = driver.find_elements_by_class_name("android.widget.TextView")
print(classall)
print(len(classall))
for title in classall:
    print(title.text)

classall[1].click()  #取元素组里面的任意值进行取值并操作

# 通过 xpath 方法定位一组元素

xpathall = driver.find_elements_by_xpath("//*[contains(@text,'tooth')]")
print(len(xpathall))
print(xpathall)
for i in xpathall:
    print(i.text)

xpathall[0].click()

time.sleep(5)

driver.quit()