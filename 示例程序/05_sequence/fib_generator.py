#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def fib(n):
    '''accept an integer n.
       return the numbers less than n in Fibonacci sequence.
    '''
    prev, curr = 1, 1
    while prev < n:
        print(prev, end=' ')
        prev, curr = curr, prev + curr
    print()

def test_fib( ):
    n = int(input('请输入整数n:'))
    fib(n)

# 生成器函数
def fib2():
    prev, curr = 1, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

a = fib2()
for i in range(10):
   print(next(a), end=' ')
print()


if __name__ == '__main__':
    count = 0
    for i in fib2():
        if i > 1000:
            break
        print(i, end='\t')
        count += 1
        if count % 5 == 0 :
            print()

    if count % 5:
        print()

