#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import string
import random

""" 课堂上我们介绍了如何使用字典来统计一段文本中各个字母出现的次数。
现在我们希望统计英文字母以及数字的出现次数，英文字母统计时大小写无关，
另外所有数字统一计数。最后输出其中出现次数最高的前10位字符以及出现的次数。

输出结果如下所示：

字母	次数
数字	101
g	33
q	30
m	28
n	27
z	27
i	26
o	25
b	24
c	24

"""

def letter_counter(seq):
    return {}


def topn_letters(counters, n=10):
    """
    字母	次数
    数字	101
    g	33
    q	30
    m	28
    n	27
    z	27
    i	26
    o	25
    b	24
    c	24
    # counters = { 'a': 4, .... 'z':5, 'digits':4}
    """
    pass


if __name__ == '__main__':
    x = string.ascii_letters + string.digits + string.punctuation
    text = [random.choice(x) for i in range(1000)]
    text = ''.join(text)

    counters = letter_counter(text)
    topn_letters(counters)

# __import__('sys').exit(0)
