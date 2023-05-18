"""
在密码学中，有一种替换加密方法，其基本思想是将一个字符用另一个字符替代
   考虑如下密码算法，如果文本中的字符为（小写/大写）英文字母，则该字母替代为另一个(小写/大写）英文字母，如果不是英文字母，则原样输出。
   1 首先使用random模块的相应函数产生一个随机的密码本
   2 实现加密和解密函数

"""

import string
import random

ascii_lower = string.ascii_lowercase

def key():
    return ascii_lower

crypt_map = key()

def enc(text, key=crypt_map):
    return text

def dec(text, key=crypt_map):
    return text


if __name__ == '__main__':
    print('替换加密:\n{}\n{}'.format(ascii_lower, crypt_map))
    text1 = enc("Luck is a dividend of sweat. The more you sweat, the luckier you get.")
    print(text1)
    text2 = dec(text1)
    print(text2)
