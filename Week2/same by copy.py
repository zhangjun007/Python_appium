#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/24 15:47

#该内容是通过浅copy创造一个夫妻之间的联动账户，形成数据通用的效果
import copy

person=["name","age",["monkey",100000],"Phone number"]  #定义一个公共账户

person1=copy.copy(person)      #将公共账户关联到person1
person2=copy.copy(person)      #将公共账户关联到person2

person1[0]="张军"             #修改person1的所有人
person2[0]="侯宪冬"           #修改person2的所有人

person1[2][1]=50000           #修改任意值

print(person1)
print(person2)
