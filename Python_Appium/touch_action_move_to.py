#当前作者：jun-z  
#当前系统日期时间：2020/6/11  15:11 
#脚本名称：touch_action_move_to

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

#需求：进入密码设置界面修改手势解锁密码

#进入设置，点击进入安全界面；

security_button=driver.find_element_by_xpath("//*[@text='Security & Location']") #找到Security & Location按钮

TouchAction(driver).tap(security_button).perform()   #执行点击功能

#进入安全界面后点击锁屏菜单

screen_lock_button=driver.find_element_by_xpath("//*[@text='Screen lock']") #找到Security & Location按钮

TouchAction(driver).tap(screen_lock_button).perform()   #执行点击功能

#输入正确的手势密码

#从一个坐标移动到另外一个坐标
TouchAction(driver).press(x=100,y=351).move_to(x=300,y=456).move_to(x=688,y=4677).move_to(x=988,y=688).release().perform()

#从一个元素移动到另外一个元素

TouchAction(driver).press(元素1).move_to(元素1).move_to(元素2).release().perform()

#针对超长代码可以用两种方法 换行

#括号换行再回车
(TouchAction(driver).press(x=100,y=351)
 .move_to(x=300,y=456).move_to(x=688,y=4677)
 .move_to(x=988,y=688)
 .release().perform())
#回车换行
TouchAction(driver).press(x=100,y=351)\
    .move_to(x=300,y=456).move_to(x=688,y=4677)\
    .move_to(x=988,y=688)\
    .release().perform()