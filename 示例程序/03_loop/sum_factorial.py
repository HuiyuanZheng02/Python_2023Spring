#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def sum_factorial(n):
    ''' 求0! + 1!+2!+3!+...+n!的和 '''
    i = 1
    total = item = 1
    while i <= n:
        item *= i
        total += item
        i += 1

    return total

def sum_factorial_forloop(n):
    ''' 求0! + 1!+2!+3!+...+n!的和 '''
    total = item = 1
    for i in range(1, n+1):
        item *= i
        total += item
        # i += 1    # 这一行如果执行也不会带来别的问题

    return total


if __name__ == '__main__':
    result = sum_factorial(20)
    print('0!+1!+2!+3!+...+20!=', result)

    print('-' * 40)
    result = sum_factorial_forloop(20)
    print('0!+1!+2!+3!+...+20!=', result)
