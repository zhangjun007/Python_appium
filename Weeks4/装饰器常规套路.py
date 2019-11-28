#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/5/6 19:08

#需求描述
#1.使用装饰器功能，统计test2和test1的运行时间
#2.给test2传入参数

import time

def timmer(func):
    def deco(*args,**kwargs): #包含所有可带参数或不带参数的函数
        start_time=time.time()
        func(*args,**kwargs)  #包含所有可带参数或不带参数的函数
        stop_time=time.time()
        print("the func run time is%s"%(stop_time-start_time))
    return deco

@timmer
def test1():
    time.sleep(1)
    print("let me sleep 3 seconds")
@timmer
def test2(name,age): #函数传值需求
    time.sleep(3)
    print("test2 name is",name)
    print("test2 age is",age)

test1()
test2("der姐",18)  #调用函数时需要传入值