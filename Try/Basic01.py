#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2019/2/28 13:59

###################################################

#变量赋值
name='zhangjun'
name_7=name
NAME='houzi'

print(name_7,name,NAME)

name='houzi'
NAME='houzi1'

print(name,name_7,NAME)


###########################################################

#input 语法
name=input('Your name is:')
age=int(input('Your age is:'))
job=input('Your job is:')
salary=int(input('Your salary is:'))

info=" =====name:%s age:%s job:%s salary:%s" %(name,age,job,salary)

print(info)



#############################################

#判断年龄，猜三次

age=18
count=0

while count <3:
    guess_age=int(input("Please input your age:"))
    if guess_age > age:
        print("too old")
    elif guess_age < age:
        print("too young!")
    else:
        print("bingo!")
        break
    count+=1
    
else:
    print("too many times")
    


##################################


#for 循环 猜年龄

age = 18

for i in range(3):
    guess_age=int(input("Input your age:"))
    if guess_age >age:
        print("too young")
    elif guess_age < age:
        print("too old")
    else:
        print("bingo")
        break



# 判断年龄，猜三次后继续猜

age = 18
count = 0

while count < 3:
    guess_age = int(input("Please input your age:"))
    if guess_age > age:
        print("too old")
    elif guess_age < age:
        print("too young!")
    else:
        print("bingo!")
        break
    count += 1
    if count ==3:
        guess_again=input("Did you want to try again?")
        if guess_again !="enter":
            count=0
#else:
#    print("too many times")



