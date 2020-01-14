#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 14:00

from appium import webdriver


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

driver.implicitly_wait(10)

#首次启动确认权限
permission_button=driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")  #权限弹窗

permission_button.click()  #权限弹窗点击1

time.sleep(1) #等待弹窗

permission_button.click()  #权限弹窗点击2

#首次启动跳过推荐页
driver.find_element_by_id("com.tcl.live:id/skip_btn").click()



#使用代码操作元素，产生一些动作 ,元素 点击 实例

#一、打开 apps按钮，点击 搜索按钮；

driver.find_element_by_id("com.tcl.live:id/searchBtn").click()


#二、点击输入框，输入 内容，然后清空内容

#点击输入框
driver.find_element_by_id("com.tcl.live:id/searchWord").click()
time.sleep(2)

#输入内容
driver.find_element_by_id("com.tcl.live:id/etSearch").send_keys("love")
time.sleep(2)


#清空输入内容
driver.find_element_by_id("com.tcl.live:id/etSearch").clear()


#三、获取文本内容  element.text

app_title = driver.find_elements_by_id("com.tcl.live:id/app_title")   #将元素id值为com.tcl.live:id/app_title 统计为一个列表

print(len(app_title))  #统计该属性的 内容长度

for i in app_title:
    print(i.text)    #获取文本内容

app_title[1].click()  #点击列表内第一个元素


#四、获取 元素 的位置  和 大小；

search_button = driver.find_element_by_id("com.tcl.live:id/searchBtn")   #找到 搜索按钮元素

print(search_button.location)   # 获取搜索按钮的位置 信息
print(search_button.location["x"])
print(search_button.location['y'])


print(search_button.size)  #获取搜索按钮元素的 大小
print(search_button.size["width"])
print(search_button.size["height"])



time.sleep(3)

driver.quit()


