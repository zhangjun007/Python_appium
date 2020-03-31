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
#从AC界面启动settings
driver.start_activity('com.android.settings','com.android.settings.Settings')

#找到search按钮并点击

driver.find_element_by_xpath("//*[@content-desc='Search settings']").click()

#输入指定内容

driver.find_element_by_id("android:id/search_src_text").send_keys("light")

#点击更多按钮
driver.find_element_by_xpath("//*[@content-desc='More options']").click()

#选择清除历史输入记录按钮；

driver.find_element_by_android_uiautomator('new UiSelector().text("Clear history")').click()

#选择X掉输入的搜索内容

driver.find_element_by_id("android:id/search_close_btn").click()

#重新输入搜索内容

driver.find_element_by_id("android:id/search_src_text").send_keys("Battery")


driver.quit()

