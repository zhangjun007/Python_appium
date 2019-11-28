#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/4/27 14:05

name = "xixi"   #全局变量 ，代码顶层定义的变量都是全局变量
def change_name():
    name = "haha"  #局部变量只在函数局部作用域内生效
    print("我的名字01",name)
    return
change_name()
print(name)



def me():
    global name #声明name是全局变量  global
    name = "yj"  #修改name全局变量的值
    print(name)
    return
me()
print(name)

