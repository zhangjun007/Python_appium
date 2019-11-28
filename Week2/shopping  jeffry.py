#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/24 16:27

'''
程序：购物车程序

需求:

启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 
可随时退出，退出时，打印已购买商品和余额
'''

our_goods=[["Iphone X",6888],["Mi Max",1999],["samsung S8",5888],["Pixi 4-4.5",899]]    #将物品的信息存在一个列表

shoop_good  =   []       #存一个空列表到

balance = input("Please input your bank card balance:") #提示用户输入用户的银行卡余额

if  balance.isdigit():
        balance = int(balance)

        while True:

            for index, item in enumerate(our_goods):    #取出商品列表中每个商品的 下标 ，并将产品信息赋给 item
                print(index, item)                  #进行索引下标，并打印下标 和 产品信息

            goods_ID=input("Please select your product number:") #提示用户输入产品编号,并将ID赋给新的值

            if goods_ID.isdigit():
                goods_ID = int(goods_ID)
                if goods_ID < len(our_goods)  and goods_ID >= 0: #如果输入的值在区间值内  len(列表名)方法是获取列表最长下标
                    p_item = our_goods[goods_ID]   #可理解 p_item=our_goods[3]  3是用户选择的ID，此处时将该产品信息提出出来赋给p_item

                    if p_item[1] <= balance:

                        balance -= p_item[1]  #扣款步骤，并将余额赋给balance余额中
                        shoop_good.append(p_item)  # 并将提出出来的商品信息添加到 待用的 列表中
                        print("产品已经添加到您的购物车中，您的余额%s"%balance)
                    else:
                        print("your current is not enough,please choose other goods！")  #余额不够时提示
                else:
                    print("the goods is null!")

            elif goods_ID == 'q':
                print("---------shoopping list---------")
                for i in shoop_good:
                    print(i)
                print("your current is %s"%balance)
                exit()
            else:
                print("无效操作，请输入正确内容：")

print("-----------------------------------------------------分割线----------------------------------------------")



good_list1=[("PhoneX",8888),("chongqiwawa",12000),("YB",2),("bike",888),("Mi max",1999),("tesila",120000)]

shoop_good1=[]

balance1=input("please input your balance:")
if balance1.isdigit():
        balance1=int(balance1)
        while True:
            for index1,item1 in enumerate(good_list1):
                print(index1,item1)

            good_id=input("please input the good id>>:")
            if good_id.isdigit():
                good_id=int(good_id)
                if good_id < len(good_list1) and good_id >=0:
                    p_item1 = good_list1[good_id]

                    if  balance1 >= p_item1[1]:

                        balance1-=p_item1[1]
                        shoop_good1.append(p_item1)
                        print("Your product %shas been added to the shopping cartyour current balance is%s"%(p_item1,balance1))
                    else:
                        print("余额不够,先充钱，别哔哔！")

                else:
                    print("the number is null!")
            elif good_id == 'q':
                 print("shoopping list:")
                 for i in shoop_good1:
                     print(i)
                 print("your current balance is%s"%balance1)
                 exit()
            else:
                print("SyntaxError: invalid syntax")













