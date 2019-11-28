#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/2/5 16:57

#猜测年龄：
#1.输入年龄，对比年龄大小，大提示太大，小提示太小，输入年龄正确提示正确；
#2.猜测超过3次都错误，直接提示次数太多


age_of_guess = 18
count=0

for i in range(3):
    input_age= int(input("请输入年龄值："))
    if input_age>age_of_guess:
        print("too old!")
    elif input_age<age_of_guess:
        print("too young!")
    else:
        print("congratulations！")
        break
    count+=1


#根据以上需求增加：猜测次数超过3次，提示是否继续猜测，用户可选择重新是否继续猜测；

age_of_guess1 = 18
count1=0

while count1 <3:
    input_age1 = int(input("请输入年龄值："))
    if input_age1 > age_of_guess1:
        print("too old!")
    elif input_age1 < age_of_guess1:
        print("too young!")
    else:
        print("confratulations!")
        break
    count1+=1
    if count1 ==3:
        again_guess = input("Do you want to retry?")
        if again_guess == 'y':
            count1 = 0
        else:
            break
