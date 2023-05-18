#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def three_digit_numbers():
    # 输出由1、2、3、4这四个数字组成的每位数都不相同的所有三位数。
    digits = (1, 2, 3, 4)
    for i in digits:
        for j in digits:
            for k in digits:
                if i != j and j != k and i != k:
                    print(i * 100 + j * 10 + k)

# from math import sin as loc_sin

def three_digit_numbers2():
    digits = (1, 2, 3, 4)
    for i in digits:
        for j in digits:
            if i == j: continue
            for k in digits:
                if j != k and i != k:
                    print(i * 100 + j * 10 + k)

def three_digit_numbers22():
    digits = (1, 2, 3, 4)
    for i in digits:
        i100 = i * 100
        for j in digits:
            if i == j: continue
            j10 = j * 10
            for k in digits:
                if j != k and i != k:
                    print(i100 + j10 + k)

def three_digit_numbers3():
    counts = 0
    digits = (1, 2, 3, 4)
    for i in digits:
        for j in digits:
            if i == j: continue
            for k in digits:
                if j != k and i != k:
                    print(i * 100 + j * 10 + k, end=' ')
                    counts += 1
                    if counts % 5 == 0: print()
    if counts % 5:
        print()

import time
def profiles(func1, func2, tries=5000):
    start = time.time()
    for i in range(tries):
        func1()
    stop = time.time()
    print('call function %s %d times, elapsed time(seconds): %.2f' % (func1.__name__, tries, stop-start))

    start = time.time()
    for i in range(tries):
        func2()
    stop = time.time()
    print('call function %s %d times, elapsed time(seconds): %.2f' % (func2.__name__, tries, stop-start))


if __name__ == '__main__':
    three_digit_numbers()

    print('-' * 40)
    three_digit_numbers2()

    print('-' * 40)
    three_digit_numbers3()
    print('-' * 40)
    profiles(three_digit_numbers, three_digit_numbers2, 5)


