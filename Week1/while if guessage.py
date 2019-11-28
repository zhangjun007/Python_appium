#猜测年龄：
#1.输入年龄，对比年龄大小，大提示太大，小提示太小，输入年龄正确提示正确；
#2.猜测超过3次都错误，则提示是否继续猜测，用户可选择重新是否继续猜测；

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
print("..............................")



