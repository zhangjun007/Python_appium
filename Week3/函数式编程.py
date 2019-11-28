#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/8/13 15:32


import time
def logger():
    time_formate="%Y-%m-%d %X"
    time_current=time.strftime(time_formate)
    with open("222.TEXT","a") as f:
        f.write("%s logcat:\n" %time_current)

def logcat1():
    print("1111111111111")

    logger()


def logcat2():
    print("222222222222")

    logger()


def logcat3():
    print("333333333")

    logger()