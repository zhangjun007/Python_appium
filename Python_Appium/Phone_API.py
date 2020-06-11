#当前作者：jun-z  
#当前系统日期时间：2020/6/11  16:15 
#脚本名称：Phone_API

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType


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

#获取设备的分辨率

size=driver.get_window_size()
print(size)
print(size["width"])
print(size["height"])

#设备截图

#打开任意界面，截图保存指定路径且命名

driver.get_screenshot_as_file("picture.png")   #默认脚本路径

driver.get_screenshot_as_file("F:\\Download\\anr\\toast.png") #指定路径


#获取手机网络

driver.network_connection

'''
Possible values:
            Value (Alias)      | Data | Wifi | Airplane Mode
            -------------------------------------------------
            0 (None)           | 0    | 0    | 0
            1 (Airplane Mode)  | 0    | 0    | 1
            2 (Wifi only)      | 0    | 1    | 0
            4 (Data only)      | 1    | 0    | 0
            6 (All network on) | 1    | 1    | 0
'''
#设置手机网络

driver.set_network_connection(1)

#设置手机网络 功能扩展

if driver.set_network_connection()==ConnectionType.AIRPLANE_MODE:  #此方法需要再顶部 import方法
    print(2)
else:
    print(3)


#发送键到设备

#Android Keycode ：https://blog.csdn.net/shililang/article/details/14449527

#需求  三次音量+，返回，两次音量-，桌面

driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(4)
driver.press_keycode(25)
driver.press_keycode(25)
driver.press_keycode(25)


#操作手机通知栏

driver.open_notifications()  #打开通知栏

driver.press_keycode(4) #appium没有提供专门的关闭通知栏的方法，可以按返回键来关闭


time.sleep(3)

driver.quit()