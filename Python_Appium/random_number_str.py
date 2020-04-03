#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2020/1/14 14:18

import random
import string


def get_random_str(randomlength=6):

    """
      生成一个指定长度的随机字符串，其中
      string.digits=0123456789
      string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
      """
    str_list=[random.choice(string.digits+string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

search_worlds=get_random_str()
print(search_worlds)


# for i in range(20):
#     print(search_worlds)