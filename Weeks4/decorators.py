#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/9/4 14:05

import time

def timmer(func):
    def lowser(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is%s"%(stop_time-start_time))
    return lowser

@timmer
def test1():
    time.sleep(3)
    print("houzi  gai qi chuang  niaoniao la!")

test1()