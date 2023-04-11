#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def fib(t):
    a, b = 1, 1
    while b < t:
        a, b = b, a + b
    else:
        return b


def fib(t):
    """ 返回大于t的最小fibonacci数 """
    prev, curr = 1, 1
    while curr <= t:
        prev, curr = curr, prev + curr
    return curr

if __name__ == '__main__':
    print(fib(50))
