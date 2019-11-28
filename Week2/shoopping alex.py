#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/25 13:56


product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),]       #存储一个商品列表

shopping_list = []              #存储一个空列表待用

salary = input("Input your salary:")        #用户输入薪水

if salary.isdigit():            #判断输入的数值是否是只有数字组成     # 变量.isdigit 功能就是检测内容是否是只有数字组成
    salary = int(salary)        #对输入的内容进行强制要求int类型

    while True:                 #当输入薪水类型OK时

        for index,item in enumerate(product_list):  #   1.enumerate方法  是对（）内列表 列出列表内元素的 数据 和 下标；
                                                    # 2.index索引 方法是 查找 当前列表指定位置的内容

            #print(product_list.index(item),item)
            print(index,item)       #打印出当前商品所在列表中的 下标  和  内容 ，下表赋值给index，内容赋值给 item

        user_choice = input("选择要买嘛？>>>:")       #打印信息提示用户选择买什么？让用户输入商品编号
        if user_choice.isdigit():                 #变量名.isdigit方法 ：判断用户选择的商品是否是由数值组成
            user_choice = int(user_choice)      #对用户输入进行int转换
            if user_choice < len(product_list) and user_choice >=0:     #判断用户输入的编号ID是否在 符合当前商品编号列表
                p_item = product_list[user_choice]      #并将产品编号的价钱 赋值给p_item

                if p_item[1] <= salary:             #用户的薪水数值大于产品的价格买的起
                    shopping_list.append(p_item)    #将该产品存到当前的空列表中待用
                    salary -= p_item[1]             #扣款步骤
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary) )
                        #打印当前加入购物车的产品 和 用户的余额
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)    #提示用户余额不够
            else:
                print("product code [%s] is not exist!"% user_choice)   #用户输入的产品ID不存在，提示

        elif user_choice == 'q':                #当用户输入“q”时 ，打印当前购物车列表 以及当前的余额；
            print("--------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()          #exit() 方法就是退出当前 程序
        else:
            print("invalid option")