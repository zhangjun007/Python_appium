#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/11/9 15:48

dict ={                #创建一个字典
    'per01':"18",
    'per02':"28",
    'per03':"32",
    'per04':"109",
    'per05':"205"
}

dict01={
    'per01':"29",
    'per02':"29",
    'per07': "29",
    'per08':"29",
}

#查找字典内某些KEY的Value

print(dict["per01"])  #当确认字典内有该KEY时

print(dict.get("per01"))  #当不确认字典内有该KEY时

#判断KEY值是否再字典内

print("per02" in dict01)   #返回值为 False  or  True

#修改字典内某些Key的Value

dict["per01"]="28"

print(dict)  # Key Per01的Value值已经由18变成28；

#字典中增加新的Value值

dict["per06"]="108"

print(dict)  # 字典内已经新增了一个 Key为per04 Value为108的值

#删除字典中的Key和对应的Value

del dict["per06"]   #del 字典名["KEY"]，指定删除某一KEY及Value
print(dict)

dict.pop("per05")  #字典名.pop("KEY")，指定删除某一KEY及Value
print(dict)

dict.popitem()   #字典名.popitem(),随机删除字典内任意的KEY及Value
print(dict)

#合并两个字典

dict.update(dict01) #字典1.update(字典2)，当Key相同时，对应Value被覆盖， 不同的Key会把当前直接copy放后面

print(dict)

#输出字典的 所有 KEY  or  Value

print(dict.keys())

print(dict.values())

#将字典内左右的KEY和value当成一个值，并组成一个列表
print(dict.items())



