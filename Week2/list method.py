#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/23 15:25
ages=["a","b","c","d","e","f","g"]

names=["zhangjun","houxiandong",["1","2","3"],"xiaoer","daxigua","dajiba",]
names[2]="erhuo"

names2=names.copy() #将names列表的内容copy给names2列表

names[3]="erhuo"
print(names2)
print(names)

names[2][2]="erbage"  #更改names列表中的列表的指定位置的值
print(names)
print(names2)


ages.append("h")    #增加指定值到最后一位
print(ages)

ages.insert(3,"caonima") #增加指定值到指定位置
print(ages)

ages[3]="nimabi"    #将指定位置内容更换为指定内容
print(ages)

ages.remove("nimabi")   #移除指定内容
print(ages)

del ages[3]        # 删除自定位置的内容
print(ages)

ages.pop(3)       #删除指定位置的内容，pop语法若未指定位置，默认删除最后一位
print(ages)

print(ages.index("a")) #index是索引查找， 查找改列表中指定内容的位置

ages.count("a")     #查找内容a的重复个数

ages.reverse()      #将ages列表倒叙显示

names.sort()    #将names列表按照ASCII码的列表顺序显示

ages.extend(names)  #将names列表 并入到ages列表，且names列表并不会消失
print(ages)


