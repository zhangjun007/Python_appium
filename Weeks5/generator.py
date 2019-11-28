#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/5/10 16:02

#列表生成器： 运行生成器之后，会生成一个内存地址，但并不存在数据，只有调用到该方法时会通过设定的算法生成对应的数据；
#            不调用不存在，调用才生成数据；


c=[i*2 for i in range (1000)]  #列表生成式


c=(i*2 for i in range (1000))  #生成器   ，生成器是() ，生成式是[]

print(c)         #c是一个内存地址，并不存在数据 晕性结果<generator object <genexpr> at 0x0000017B66DEF830>


c.__next__()  #只能一个一个获取，不知前不知后，只保留当前位置的值


#使用函数实现斐波那契数列

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return "done"

fib(100)   #可生成100个斐波那契数据列

#使用yield方式 即可变成生成器


def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield(b)
        a,b=b,a+b
        n=n+1
    return "done"

#
print(fib(100))
#run ：<generator object fib at 0x000001BA65A7F830>

f=fib(100)
print(f.__next__()) #获取第一个值

print("=====可出来做其他事情")

print(f.__next__()) #获取第二个值

print("=====打断===== ")

# 通过for 循环

for i in f:
    print(i)


