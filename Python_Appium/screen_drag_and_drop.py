#当前作者：jun-z  
#当前系统日期时间：2020/4/15  11:39 
#脚本名称：screen_drag_and_drop

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

#进入首页，左滑屏进入第二个Tab
windows_size=driver.get_window_size()
print(windows_size)

x=driver.get_window_size()["width"]
y=driver.get_window_size()["height"]
print(x,y)

driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 500)

time.sleep(3)
print("左滑屏结束，进入到第二个Tabl")

#drag_and_drop方法

driver.implicitly_wait(8)
more_button = driver.find_elements_by_id("com.tcl.live:id/subject_more")  #元素1
for i in more_button:
    print(i.text)
button01 = more_button[0]

install_button = driver.find_elements_by_id("com.tcl.live:id/app_icon")
for i in  install_button:
    print(i.text)
button02 = install_button[5]  #元素2

print("开始拖动元素")
driver.drag_and_drop(button02,button01)
print("拖动元素完成")

time.sleep(5)

driver.quit()