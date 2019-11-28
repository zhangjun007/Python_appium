#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/23 14:35
for i in range(0,100,3):
    print("time:",i)



count =0
guessage=18

while True:
    age=int(input("guess my age:"))
    if age ==guessage:
        print("great,you are rigth!")
        break
    elif age > guessage:
        print("too young!")
    else:
        print("too old")
    count+=1
    if count == 3:
        confirm = input("do you wanr try agin?")
        if confirm == 'enter':
            count = 0
    if  age < guessage:
        print("you guess too many times,fuck off, you can go out!")
        break


'''else:
    confirm= input(print("again?"))
    if confirm=='enter':
        for i in range (3):
    else:
        break
'''
