#当前作者：jun-z  
#当前系统日期时间：2020/6/11  14:27 
#脚本名称：touch_action_wait

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
desired_caps["appPackage"] = 'com.android.settings'
desired_caps["appActivity"] = 'com.android.settings.Settings'
desired_caps['UDID'] = 'P7CAVSQGJ7EYMJB6'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(2)


driver.implicitly_wait(20)
#需求进入设置-wifi-长按一个wifi选项

#进入Network选项并点击
Net_button=driver.find_element_by_xpath("//*[@text='Network & connection']")
TouchAction(driver).tap(Net_button).perform()

#选择Wifi并点击
WIFI_button=driver.find_element_by_xpath("//*[@text='Wi-Fi']")
TouchAction(driver).tap(WIFI_button).perform()

#选择OA wifi持续3s后松开

OA_WIFI_button=driver.find_element_by_xpath("//*[@text='TCT-OA']")
TouchAction(driver).press(OA_WIFI_button).wait(3000).release().perform()



time.sleep(5)

driver.quit()