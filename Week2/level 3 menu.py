#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/11/23 15:30

#作业要求:

#1.打印省、市、县三级菜单
#2.输入省份后会返回省份对应的城市；
#3.输入城市后会返回城市对应的县城
#4.可返回上一级
#5.可随时退出程序

data = {
    '深圳':{
        "南山区":{
            "大冲":["联想","甲骨文"],
            "深大":["Tencent","深圳大学"]
        },
        "福田区":{},
        "罗湖区":{}
            },
    '广州':{
        "白云区":{},
        "番禺区":{}
            }
       }
exit_flag=False
while not exit_flag:
    for i in data:
        print(i)

    choice = input("请输入一级城市名称:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("请输入二级区名称:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)

                    choice3 = input("请输入三级地名称:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t",i4)

                        choice4 = input("Press b to back:")
                        if choice4 =='b':
                            pass
                        elif choice4 =='q':
                            exit_flag= True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 =='b':
                break
            elif choice2 == 'q':
                exit_flag = True
