#当前作者：jun-z  
#当前系统日期时间：2020/6/11  13:45 
#脚本名称：touch_action_press_release

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


driver.implicitly_wait(20)

#需求 指定一个元素按下
apps_button=driver.find_element_by_xpath("//*[@text='APPS']")
TouchAction(driver).press(apps_button).perform()

#需求 指定一个元素按下后抬起
apps_button=driver.find_element_by_xpath("//*[@text='APPS']")
TouchAction(driver).press(apps_button).release().perform()

#需求 指定一个坐标按下
TouchAction(driver).press(x=505,y=1292).perform()

#需求指定一个坐标按下后抬起
TouchAction(driver).press(x=505,y=1292).release().perform()

time.sleep(5)

driver.quit()