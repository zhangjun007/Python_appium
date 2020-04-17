#当前作者：jun-z  
#当前系统日期时间：2020/4/15  10:01 
#脚本名称：screen_operater_scroll

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '8.1.0'
desired_caps["deviceName"] = 'localhost'
desired_caps["appPackage"] = 'com.tcl.live'
desired_caps["appActivity"] = 'com.tcl.live.activity.MainActivity'
desired_caps['UDID'] = 'd424d295'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

#元素到元素之间的滑动

button01 = driver.find_element_by_id("com.tcl.live:id/searchBtn")  #元素1
print("已取到元素1的Text：%s"%button01.text)

driver.implicitly_wait(5)
button02 = driver.find_element_by_id("com.tcl.live:id/subject_more")  #元素2
print("已取到元素2的Text：%s"%button02.text)

driver.scroll(button02,button01,3000)  #从元素2滑动到元素1的位置
print("已从元素2滑动到元素1")

time.sleep(3)
print("等待3秒")

button_more = driver.find_elements_by_id("com.tcl.live:id/app_icon")
for i  in button_more:
    print(i.text)
button03 = button_more[2]  #取到当前页面的元素3
print("已取到元素3的Text：%s"%button03.text)

button04 = button_more[7]  #取到当前页面的元素4
print("已取到元素4的Text：%s"%button04.text)

driver.scroll(button04,button03,3000)  #从元素4滑动到元素3
print("已从元素4滑动到元素3")

time.sleep(3)
print("等待3秒")

#继续取当前页面的新的元素
button_more = driver.find_elements_by_id("com.tcl.live:id/app_icon")
for i  in button_more:
    print(i.text)

button05 = button_more[2]  #取到当前页面的元素5
print("已取到元素5的Text：%s"%button05.text)

button06 = button_more[8]  #取到当前页面的元素6
print("已取到元素6的Text：%s"%button06.text)


driver.scroll(button06,button05,3000)  #从元素6滑动到元素5的位置

print("已从元素6滑动到元素5")


time.sleep(5)


driver.quit()
