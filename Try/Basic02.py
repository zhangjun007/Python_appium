#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/2/28 15:29

'''
###################
#二进制转换 decode 和 encode

name="张军，你好帅"

print(name.encode(encoding="utf-8"))

print(name.encode(encoding="utf-8").decode(encoding="utf-8"))
'''

#####################
#列表的简历和使用
age=18
name=[1,"Jun",age,age+1]
print(name)

#列表取值
print(name[2])
#列表取多个值
print(name[0:100])
#列表倒叙取值
print(name[-3:-1])
print(name[-3:])
print(name[-1])

#列表增加值
name.append("Hou")
print(name)

#列表指定位置增加值
name.insert(1,"Money")
print(name)

#将列表指定位置更换内容
name[1]="Fuck"
print(name)

#删除列表中指定内容