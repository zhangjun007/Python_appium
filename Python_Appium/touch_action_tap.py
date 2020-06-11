#当前作者：jun-z  
#当前系统日期时间：2020/4/17  13:30 
#脚本名称：touch_action_tap

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

import time
import random
import string
import datetime

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

time.sleep(2)

#使用步骤
#1.创建touchaction对象
#2.通过对象调用想执行的手势
#3.通过perform()执行动作

#手指轻敲的动作,tap(元素)

driver.implicitly_wait(20)

#需求：点击Apps，点击 Action Tag按钮
apps_button=driver.find_element_by_xpath("//*[@text='APPS']") #找到apps按钮

TouchAction(driver).tap(apps_button).perform()   #执行点击功能

tag_button=driver.find_element_by_xpath("//*[@text='Action']")  #找到Action菜单

TouchAction(driver).tap(tag_button).perform()  #执行点击


#手指轻敲的动作,tap(坐标)实现

TouchAction(driver).tap(x=505,y=1292).perform()

#手机轻敲，重复次数 tap(坐标/元素，count=n)

apps_button=driver.find_element_by_xpath("//*[@text='APPS']") #找到apps按钮

TouchAction(driver).tap(apps_button,count=2).perform()   #执行点击功能


time.sleep(5)

driver.quit()