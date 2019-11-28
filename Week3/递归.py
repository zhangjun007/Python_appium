#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/8/23 15:07

#递归的特性：
#1.必须要有一个结束条件；
#2.递归过程中传进去的值必须是层层减少；
#3.递归层次过多会造成栈溢出，应该减少递归的使用；

def icon(n):
    print(n)
    if int(n/2)>0:
        return icon(int(n/2))
    print("---->",n)
icon(100)