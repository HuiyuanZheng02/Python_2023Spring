#!/usr/bin/env python3

import math

"""
for condidate in possible_condidates:
    ...
    if satisifed(condidate):
        found(condidate)
        break

for condidate in possible_condidates:
    ...
    if satisifed(condidate):
        found(condidate)
"""

def is_prime0(n):
    prime = True
    for factor in range(2, n):
        if n % factor == 0:
            prime = False
            break

    return prime


def is_prime(n):
    ''' 判断一个数是否为素数
    >>> n = int(input("Input a integer:"))
    >>> print(is_prime(n))
    '''
    prime = True
    max_factor = int(math.sqrt(n) + 1)
    for factor in range(2, max_factor): # 检查可能的因子
        if n % factor == 0:             #如果有非1的因子，则n不是素数
            prime = False
            break

    return prime


def max_prime(limit=100):
    # 寻找100以内的最大素数

    for n in range(limit, 1, -1):
        max_factor = int(math.sqrt(n) + 1)
        for factor in range(2, max_factor):
            if n % factor == 0:
                break
        else:
            print(n)
            break

def all_primes(limit=100):
    # 寻找100以内的所有素数

    for n in range(limit, 1, -1):
        max_factor = int(math.sqrt(n) + 1)
        for factor in range(2, max_factor):
            if n % factor == 0:
                break
        else:
            print(n, end=' ')
    print()


if __name__ == '__main__':
    n = int(input("Input a integer:"))
    print(is_prime(n))

    max_prime()
    all_primes()

