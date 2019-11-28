#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/11/22 15:07

person001 = {
    "Europe":{
        "jeffry": ["handsome","182cm","68kg"],
            },
    "japan":{
        "wutenglan":["famous","45kg","158cm"]
            },
    "china":{
        "linzhiling":["tall","172cm","60kg"]
            }
}                                  #person001字典内嵌套了Europe 、japan、三个字典。 以上每个字典内又嵌套了一个字典

person001["japan"]["wutenglan"][1] = "48kg" #修改字典内指定下标的值

person001.setdefault("china",{"linzhiling":["renyao","beautiful","noman"]})
#setdefault语法是找寻字典内指定的key，将后面的内容替代掉，若无指定的key则直接新建一个字典

print(person001)


person002=dict.fromkeys(["key1","key2","key3"],{"names":["jeffry","28","handsome"]})
#dict.fromkeys语法是指定key or value

person002["key2"]["names"][1]="18"  #按照fromkeys语法来修改value值，会将所有的value值全部改掉，此坑谨记

print(person002)