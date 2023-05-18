#!/usr/bin/env python3

def find_narcissi_few():
    '''输出“水仙花数”。
    所谓水仙花数是指1个3位的十进制数，其各位数字的立方和等于该数本身。
    例如：153是水仙花数，因为153 = 1^3 + 5^3 + 3^3
    '''

    for i in range(100, 1000):
        ones = i % 10
        tens = i // 10 % 10
        hundreds = i // 100
        if ones ** 3 + tens ** 3 + hundreds ** 3 == i:
            print(i)


def find_narcissi_few2():
    '''输出“水仙花数”。
    所谓水仙花数是指1个3位的十进制数，其各位数字的立方和等于该数本身。
    例如：153是水仙花数，因为153 = 1^3 + 5^3 + 3^3
    '''

    for hundreds in range(1, 10):
        for tens in range(10):
            for ones in range(10):
                n = ones + 10 * tens + 100 * hundreds
                if ones ** 3 + tens ** 3 + hundreds ** 3 == n:
                    print(n)


def find_narcissi_few3():
    result = [i for i in range(100, 1000)
              if (i % 10) ** 3 + (i // 10 % 10) ** 3 + (i // 100) ** 3 == i]
    print('三位水仙花数:', *result)


if __name__ == '__main__':
    find_narcissi_few()

    print('-' * 40)
    find_narcissi_few2()

    print('-' * 40)
    find_narcissi_few3()
