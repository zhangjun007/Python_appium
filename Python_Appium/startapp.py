from appium import webdriver

import time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '8.1.0'
desired_caps["deviceName"] = '192.168.9.103:5555'
desired_caps["appPackage"] = 'com.android.settings'    #需要测试的app都在前置代码中写明了
desired_caps["appActivity"] = 'com.android.settings.Settings'
desired_caps['UDID'] = 'P7CAVSQGJ7EYMJB6'
desired_caps['noReset']  =  "True"
desired_caps['unicodeKeyboard']  =  "True"
desired_caps['resetKeyboard']  =  "True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#启动要测试的app代码
#通过adb shell dumpsys window | findstr mCurrentFocus 查看
driver.start_activity("com.tcl.live",'com.tcl.live.activity.MainActivity')

time.sleep(3)

print("----------即将退出")

#关闭app，但是driver驱动不会被关闭
driver.close_app()

#关闭ap，driver驱动也被关闭了
driver.quit()
