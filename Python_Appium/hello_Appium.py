#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/12/30 15:39


from appium import webdriver
import  time

desired_caps = dict()
desired_caps["platformName"] = 'Android'
desired_caps["platformVersion"] = '7.0'
desired_caps["deviceName"] = '192.168.9.103:5555'
desired_caps["appPackage"] = 'com.tcl.live'
desired_caps["appActivity"] = 'com.tcl.live.activity.MainActivity'
desired_caps['UDID'] = 'SSDA5L5SQWV8HEHU'  #调试真机 adb devices 的值即可

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# 以上代码是固定格式和内容的，若要测试不同设备只需要修改其参数即可

time.sleep(3)

driver.close_app()  #只是退出当前界面，后台进程还在

# driver.quit()  #退出当前进程，包括后台

print(driver.current_package)