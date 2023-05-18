#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def print_triangle():
    lines = int(input('请输入n:'))

    for i in range(lines):
        for j in range(i + 1):
            print('*', end='')
        print()
    print()

    for i in range(lines):
        stars = '*' * (i + 1)
        print(stars)
    print()

    for i in range(lines):
        stars = ' '.join('*' * (i + 1))
        print(stars)
    print()

    # n stars + n-1 spaces
    for i in range(lines):
        stars = ' '.join('*' * (i + 1))
        line = stars.rjust(lines * 2 - 1, ' ')
        line = '{: >{}}'.format(stars, lines * 2 - 1)
        print(line)

    
if __name__ == '__main__':
    print_triangle()
