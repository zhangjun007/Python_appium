#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/11/23 14:49

person001 = {
    "Europe":"jeffry",
    "japan":"wutenglan",
    "china":"linzhiling"
}

for key in person001:
    print(key)    #打印person字典中的key

    print(person001[key])  #打印person字典中的value

    print(key,person001[key])