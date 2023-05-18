#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import string
import random
try:
    import matplotlib.pyplot as plt
except:
    plt = None

""" 课堂上我们介绍了如何使用字典来统计一段文本中英文字母出现的次数。
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
    counters = dict()
    for item in seq:
        if item.isalpha():
            item = item.lower()
            counters[item] = counters.get(item, 0) + 1
        elif item.isdigit():
            counters['digit'] = counters.get('digit', 0) + 1
    return counters


def topn_letters(counters, n=10):
    print(counters)
    # 排序，基于次数，都相同时基于字母顺序

#    counters_sorted = sorted(counters, key=lambda x: (counters[x], x), reverse=True)
    counters_sorted = sorted(counters, key=lambda x: (counters[x], -ord(x) if x != 'digit' else 0), reverse=True)
    # i j  28 
    # t  27

    topn = counters_sorted[:n]

    print('%s\t%s' % ('字母', '次数'))
    for key in topn:
        print('%s\t%s' % (key if key != 'digit' else '数字', counters[key]))

    plot_counter([counters[key] for key in topn], topn)

def plot_counter(values, labels):
    if not plt: return
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_title('letter counters', fontsize=14, fontweight='bold')
    ax.bar(labels, values)
    ax.set_yticks(range(0, max(values)+1, 10))
    ax.grid(axis='y', linestyle='--', color='0.75')
    plt.show()


if __name__ == '__main__':
    x = string.ascii_letters + string.digits + string.punctuation
    text = [random.choice(x) for i in range(1000)]
    text = ''.join(text)

    counters = letter_counter(text)
    topn_letters(counters)

    print('-' * 60)
    counters2 = letter_counter2(text)
    topn_letters2(counters2)


# __import__('sys').exit(0)
