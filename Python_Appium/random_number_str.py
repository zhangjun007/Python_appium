#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 14:18

def get_random_number_str(length):
    """
    生成随机数字字符串
    :param length: 字符串长度
    :return:
    """
    num_str = ''.join(str(random.choice(range(10))) for _ in range(length))
    return num_str
print(num_str)