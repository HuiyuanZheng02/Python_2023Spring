#!/usr/bin/env python3

def extract_digits_noloop(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字"""

    place = 1  # 右边数起第几位

    digit = num % 10
    print('右边数起第%d位数字为%d' % (place, digit))
    place = place + 1
    num = num // 10
    if num == 0:
        return

    digit = num % 10
    print('右边数起第%d位数字为%d' % (place, digit))
    place = place + 1
    num = num // 10
    if num == 0:
        return

    digit = num % 10
    print('右边数起第%d位数字为%d' % (place, digit))
    place = place + 1
    num = num // 10
    if num == 0:
        return

    print('剩余数字:', num)


def extract_digits(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字"""

    place = 1  # 右边数起第几位

    while True:
        digit = num % 10
        print('右边数起第%d位数字为%d' % (place, digit))
        place = place + 1
        num = num // 10
        if num == 0:
            break


def extract_digits2(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字"""

    place = 1  # 右边数起第几位
    if num == 0:
        print('右边数起第1位数字为0')

    while num != 0:
        digit = num % 10
        print('右边数起第%d位数字为%d' % (place, digit))
        place = place + 1
        num = num // 10

def extract_digits3(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字"""

    place = 1  # 右边数起第几位
    done = False
    while not done:
        digit = num % 10
        print('右边数起第%d位数字为%d' % (place, digit))
        place = place + 1
        num = num // 10
        if num == 0:
            done = True

def sum_digits(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字，然后求和"""

    place = 1  # 右边数起第几位
    digits = []
    while num:
        digit = num % 10
        digits.append(digit)
        place = place + 1
        num = num // 10
    return sum(digits)


def sum_digits2(num):
    """ 采用 //和 % 运算来得到从右边开始数起的各个数字，然后求和"""

    place = 1  # 右边数起第几位
    total = 0
    while num:
        digit = num % 10
#        digits.append(digit)
        total += digit
        place = place + 1
        num = num // 10
    return total


def test_extract_digits():
    num = int(input("请输入一个正整数..."))
    extract_digits_noloop(num)

    print('-' * 40)
    extract_digits(num)

    print('-' * 40)
    print("各个数字之和 =", sum_digits(num))

if __name__ == '__main__':
    test_extract_digits()
