#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def print_multiplication_table():
    ''' 打印九九乘法表 '''
    for i in range(1, 10):
        for j in range(1, i + 1):
#            print(i, '*', j, '=', i * j, end='\t')
#            print('%d * %d = %d' % (i, j, i*j), end='\t')
            print('{} * {} = {}'.format(i, j, i*j), end='\t')

        print()


if __name__ == '__main__':
    print_multiplication_table()