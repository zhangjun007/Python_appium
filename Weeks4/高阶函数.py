#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/9/4 15:14


# 高阶函数1：把一个函数名当作实参传值给另外一个函数（不修改被装饰函数的源代码，为其添加功能）；
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test(func):
    start_time=time.time()
    func()  #此刻运行的实际是 bar 的功能
    stop_time=time.time()
    print("the func run time is %s"%(stop_time-start_time))

test(bar)
#此刻 test(bar) = test(func) ,把 bar引入到test中，相当于 bar=func



#  高阶函数2：不修改被装饰函数的 调用方式；

import time
def bar1():
    time.sleep(3)
    print("emmmm")

def test2(func):
    print(func)  #打印的是bar的内存地址
    return func  #bar1的内存地址返回值

bar1=test2(bar1)  #bar1传给了func，
bar1()   #继续调用了bar1的功能






