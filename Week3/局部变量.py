#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/4/27 13:54

#局部变量
name="zhangjun"

def person(name):
    print("before change name:",name) #程序第一部走 name引用的是函数内的第一个赋值，zhangjun

    name="jun002"   #第二步在函数内改变了name的赋值

    print("after change name:",name) #此刻再次引用name就是用了新的值

person(name) #这个引用是在函数外部应用的所以应用还是初始值 zhangjun

print("--改了吗？",name)


