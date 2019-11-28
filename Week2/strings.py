#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/26 16:42
names="jun-z@tcl.com"
names1="j"
print(names.capitalize())   #capitalize()方法是将变量中内容的首字母大写: Jun

print(names.count("u")) #count("x")方法是统计变量内容中重复元素的个数 return: 1,即 u在下标为1的位置

print(names.center(5,"8")) #center(width,"x"),当变量小于指定width宽度时，打印结果会使用指定“x”去填充，return：8jun8

print(names.encode(encoding="utf-8")) #继续做了解！！！！！！！！

print(names.endswith("b"))  #endswitch(元素or字符串)，判断变量的内容是否以指定()的内容和位置 后缀结尾，返回Ture 或 False

print (names.expandtabs())  #expandtabs(空或数值)方法是将变量中的\t换行以 空格来替代"
print (names.expandtabs(16)) #"使用16个空格替换 \\t 符号: "

print(names[names.find("n"):]) #继续做了解！！！！

print(names.format())

