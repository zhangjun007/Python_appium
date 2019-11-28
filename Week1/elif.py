#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2017/10/23 10:15

guessage = 18

age_guessage=int(input("How old are you now:"))

if age_guessage > guessage:
    print("it's too old,guess again!")

elif age_guessage < guessage:
    print("it's too young,guess again!")

else:
    print("Great,that's all rigth!")


guessage2 =18

age_guessage2=int(input("How old are you:"))

if age_guessage2 > guessage2:
    print("too old,again!")

elif guessage2 > age_guessage2:
    print("too young! again")

else:
    print("Great!")
