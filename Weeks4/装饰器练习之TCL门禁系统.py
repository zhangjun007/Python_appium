#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/5/9 16:47

#1.一个装饰器有多个选择可供函数选择；
#2.不同的函数调用装饰器不同的功能逻辑；


import time
user,passwd="zhangjun","123456789"
def first_door(check_type):
    def second_door(func):
        def third_door(*args,**kwargs):
            username=input("Please input your name:").strip()
            password=input("Please input your age:").strip()
            if check_type=="zhiwen":
                if user==username and passwd==password:
                    print("\033[31;1mUser and password has passed ，Please use finger\033[0m")
                    res=func(*args,**kwargs)
                    print("请使用指纹刷门禁")
                    return res
                else:
                    exit("\033[32;1mUser and paswd is wrong\033[0m")
            elif check_type=="card":
                print("无指纹请使用刷卡方式")
        return third_door
    return second_door
def TCL():
    print("welcome to TCL")
@first_door(check_type="zhiwen")
def tongxun():
    print("welcome to tongxun")
@first_door(check_type="card")
def mibc():
    print("welcome to mibc")
TCL()
tongxun()
mibc()