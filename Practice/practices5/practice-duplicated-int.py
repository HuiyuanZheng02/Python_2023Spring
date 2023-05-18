#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
一个包含了多个整数的列表，其中正好只有一个整数重复出现，请找出该整数
比如 s = [1, 2, 3, 4, 5, 1]，只有1出现了两次，其他都只出现一次
"""
import random

def duplicated_int(s):
    pass

if __name__ == '__main__':
    s = random.sample(range(100), 19)
    s.insert(random.randrange(len(s)), s[random.randrange(len(s))])
    print(s)
    n = duplicated_int(s)
    print(n)
    
