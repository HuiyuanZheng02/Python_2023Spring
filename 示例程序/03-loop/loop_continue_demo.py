#!/usr/bin/env python3

def loop1(limit=11):
    # 输出limit以内(不包括limit)的奇数
    # 死循环
    i = 0
    while i < limit:  # [0, limit-1]
        if i % 2 == 0:
            continue
        print(i, end=' ')
        i += 1
    print()

    
def loop2(limit=11):
    # 输出[0,limit) 的奇数

    i = 0
    while i < limit:  # [0, limit-1]
        if i % 2 == 0:
            i += 1
            continue
        print(i, end=' ')   # [0,limit)范围内的奇数
        i += 1
    print()


def loop3(limit=11):
    # 输出[0,limit) 的奇数
    i = 0
    while i < limit:  # [0, limit-1]
        i += 1
        if i % 2 == 0:
            continue
        print(i, end=' ')   # [1,limit]范围内的奇数

def loop4(limit=11):
    # 输出[0,limit) 的奇数
    i = -1
    while i < limit-1:
        i += 1
        if i % 2 == 0:
            continue
        print(i, end=' ')   # [0,limit)范围内的奇数

    print()

def loop5(limit=11):
    # 输出[0,limit) 的奇数
    for i in range(limit):
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print()

def loop6(limit=11):
    # 输出[0,limit) 的奇数
    for i in range(limit):
        if i % 2 == 0:
            i += 1  # 没有用呀没有用
            continue
        print(i, end=' ')
    print()
    
if __name__ == '__main__':
    loop2()
