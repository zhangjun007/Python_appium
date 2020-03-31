from appium import webdriver

import time

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

time.sleep(3)

#调起设置应用程序

driver.start_activity('com.android.settings','com.android.settings.Settings')

#获取一组元素组成字典

titles=driver.find_elements_by_id("android:id/title")
print(len(titles))
for i in titles:
    print(i.text)

#点击Display按钮
titles[1].click()

#进入Display界面下一步操作
driver.find_element_by_android_uiautomator('new UiSelector().text("Brightness level")').click()

#在调整界面明亮度弹出菜单任意点击

driver.find_element_by_android_uiautomator('new UiSelector().text("Display brightness")').click()

