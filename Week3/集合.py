#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/3/23 14:44


#一、集合去重基本操作
list1=[3,2,3,4,5,5,6,7]  #列表中含有多个重复的值
list1=set(list1)     #set语法就是将list1变成一个已去重的集合


list2=set([3,2,55,55,66,77])    #可直接使用set包含需要操作的列表

print(list1,list2)

#二、取list1和list2的交集
list1.intersection(list2)

print(list1.intersection(list2))

#三、

