#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/9/4 16:14

import time

def timmer(func):  #func作为实参传给timer，是高阶函数的标志一   timmer(func)=timmer(test1)  func=test1
    def deco():    #函数内嵌套函数，是嵌套函数的标志
        start_time=time.time()
        func()   #run test1
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco  #return 返回函数名是高阶函数的标志二，此处实际返回的就是deco的内存地址

#综合以上 timer函数是一个 装饰器；

@timmer #此处 @timmer =test1=timmer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timmer#此处 @timmer =test1=timmer(test)
def test2():
    time.sleep(3)
    print("in the test2")

# timmer(test1) #将test1赋给了timmer，下面可print结果看出 实际是deco的内存地址
# print(timmer(test1))  #运行结果就是 deco的内存地址
#
# test1=timmer(test1)
# test1() #此处执行的实际是deco的内存地址，运行内存地址即运行了demo的代码体功能；

test1()
test2()