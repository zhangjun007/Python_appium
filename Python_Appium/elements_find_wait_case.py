#当前作者：jun-z  
#当前系统日期时间：2020/4/1  9:51
#脚本名称：elements_wait_ACcase


from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import time
import random
import string
#import io.appium.java_client.AppiumDriver
#from appium.webdriver.common.touch_action import TouchAction

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

driver.find_element_by_xpath("//*[contains(@text,'CANCEL')]").click()
print("取消桌面快捷方式")

#首次启动AC处理权限弹窗并进入到AC首页
driver.implicitly_wait(8)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() #Phone权限弹窗处理
print("点击Phone权限弹窗的确认按钮")

time.sleep(2)
#driver.implicitly_wait(8)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() #files权限弹窗处理
print("点击files权限弹窗的确认按钮")

driver.implicitly_wait(8)
driver.find_element_by_id("com.tcl.live:id/ok").click() #隐私弹窗处理
print("点击隐私弹窗的确认按钮")

# driver.implicitly_wait(8)
# driver.find_element_by_id("com.tcl.live:id/skip_btn").click() #推荐app的弹窗处理
# print("点击推荐applist的跳过按钮")

#从首页依次切换每一个Table

driver.find_element_by_id("com.tcl.live:id/new_tab_item_1").click() #进入Games界面
print("进入Games界面")
time.sleep(1)
driver.find_element_by_id("com.tcl.live:id/new_tab_item_2").click() #进入Apps页面
print("进入Apps界面")
time.sleep(1)
driver.find_element_by_id("com.tcl.live:id/tv_item_3").click() #进入Tools界面
print("进入Tools界面")
time.sleep(1)
#点进入Coco小游戏界面并返回

coco_icon=driver.find_elements_by_class_name("android.view.View")  #找到coco游戏按钮
for i in coco_icon:
    print(i.text)
coco_icon[6].click()  #点击coco游戏按钮
print("找到cocos游戏按钮点击进入Cocos游戏界面")

# driver.implicitly_wait(8)
# coco_back=driver.find_elements_by_class_name("android.widget.ImageView") #找到coco界面的back按钮
# for i in coco_back:
#     print(i.text)
# coco_back[0].click()  #点击coco界面的back键
# print("Cocos游戏界面点击返回键退出Cocos")
driver.keyevent(4)


#在Editor界面选择任意一个Banner进行点击进入，

driver.find_element_by_id("com.tcl.live:id/new_tab_item_0").click()
print("进入Editors界面")

waittime = WebDriverWait(driver, 20, 2)

banner_choice = waittime.until(lambda x: x.find_element_by_id("com.tcl.live:id/banner_img"))

banner_choice.click()  #进入任意Banner list
print("进入Banner的applist成功")

driver.implicitly_wait(8)

#选择任意可以install的应用点击install

install_app=driver.find_elements_by_xpath("//*[contains(@text,'INSTALL')]")
print(len(install_app))
for i in install_app:
    print(i.text)

install_app[0].click()
print("点击install按钮")

#点击硬件返回键退出到主页

driver.keyevent(4)
print("退出Banner到Editor主页")
#在Editor界面点击搜索框进入搜索界面后再返回到Editor主页

driver.find_element_by_id("com.tcl.live:id/searchWord").click()  #进入搜索界面
print("进入Editors界面的搜索界面")
driver.find_element_by_id("com.tcl.live:id/back") #退出搜索界面
print("退出Editors的搜索界面")

#进入Games界面进入Game Tags界面选中第三个Tag点击进入再返回到Games页面；

driver.find_element_by_id("com.tcl.live:id/new_tab_item_1").click() #进入Games界面
print("进入Games界面")

driver.implicitly_wait(8)
tags3=driver.find_elements_by_id("com.tcl.live:id/title") #进入第三个Tag
for i in tags3:
    print(i.text)
tags3[2].click()  #点击第三个tag
print("点击Games的第三个Tag并进入")


driver.keyevent(4)   #点击硬件back键退出第三个tag
print("点击硬件back按钮退出第三个Tag，停留在Games页面")

#以上语句可以使用driver.find_element_by_id("com.tcl.live:id/title").click()代替，但是UIAutomator一直抛出异常，后期再解决

#在Games界面点击搜索框进入搜索界面后返回到Games页面

driver.find_element_by_id("com.tcl.live:id/searchWord").click()  #进入搜索界面
print("进入Games的搜索界面")

driver.find_element_by_id("com.tcl.live:id/back") #退出搜索界面
print("退出Games的搜索界面")

#进入Tools界面进入Updatelist中，取消勾选前三项，对第四项按钮取消勾选再进行选中，退出Update界面；

driver.find_element_by_id("com.tcl.live:id/tv_item_3").click() #进入Tools界面
print("进入Tools界面")
driver.find_element_by_id("com.tcl.live:id/tv_update_more").click()  #点击进入update的applist中
print("进入update界面")

update_check=driver.find_elements_by_id("com.tcl.live:id/update_check")
for i in update_check:
    print(i.text)
update_check[0].click() #取消勾选第一项
print("取消勾选第一项")
update_check[1].click() #取消勾选第二项
print("取消勾选第二项")
update_check[2].click() #取消勾选第三项
print("取消勾选第三项")

update_check[3].click() #取消勾选第四项
print("取消勾选第四项")
update_check[3].click() #再选中第四项
print("重新勾选第四项")

driver.find_element_by_id("com.tcl.live:id/back").click()  #退出Update界面
print("退出update界面")

#进入Apps主页，进入第一个专题，并点击搜索按钮进入搜索界面；

driver.find_element_by_id("com.tcl.live:id/new_tab_item_2").click() #进入Apps页面
print("进入apps界面")
driver.implicitly_wait(5) #进入之后隐式等待5s，加载界面

apps_more = driver.find_elements_by_id("com.tcl.live:id/subject_more")
apps_more[1].click()  #进入第一个专题列表里面
print("进入第一个专题列表")

driver.find_element_by_id("com.tcl.live:id/iv_search").click() #点击搜索按钮
print("点击搜索按钮")
#随机输入内容并删除内容，重复操作20次之后返回到Apps主页

#随机生成 字符 输入后再删除

count = 0
while True:
    def get_random_str(randomlength=6):
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str
    search_worlds = get_random_str()
    print("开始输入内容----%s"%search_worlds)
    driver.find_element_by_id("com.tcl.live:id/etSearch").send_keys(search_worlds)
    print("开始删除内容----%s"%search_worlds)
    driver.find_element_by_id("com.tcl.live:id/del").click()
    count=count+1;
    if count > 20:
        break
driver.find_element_by_id("com.tcl.live:id/back").click()
print("点击返回键退出搜索界面")
driver.find_element_by_id("com.tcl.live:id/title").click()
print("点击返回键退出专题列表界面")

driver.quit()



