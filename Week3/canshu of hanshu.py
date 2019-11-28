#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/8/22 14:11


#关键字参数
def test(x,y):
    print(x)
    print(y)

test(y=2,x=1)  #此种赋值方式与形参的顺序无关

test(2,1)   #赋值时与形参的位置一一对应

test(3,y=2) #关键参数不能写在位置参数前面的

#默认参数
def test1(x,y=4):
    print(x)
    print(y)

test1(3,5)


#接收N个位置参数，转换成元组的形式  *args

def test2(*args):  # *号是固定的， args变量名随意定义  ，*变量即表示形参不固定
    print(args)

test2(1,2,3,4,5,6,7)


#接收N个关键字参数，转换成字典的方式： **kwargs

def test3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test3(name="张军",age=18,sex="M")
test3(**{'name':'张军','age':18,'sex':'M'})


#和其他参数一起使用

#位置参数一起使用
def test4(name,**kwargs):   
    print(name)
    print(kwargs)

test4('zhangjun',age=18,sex='M')



#不同参数一起使用
def test5(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test5('zhangjun',age=34,sex='M',hobby='iphone')
