#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def words_sort():
    """任意输入三个英文单词，按照字典顺序重新排列
       目的：另外一种多个输入方法，变量值交换
    """
#    s = input('x,y,z=')
#    x, y, z = s.split(',')

    text = input('请输入三个英文单词，以空格分割==>')
    x, y, z = text.split()[:3]
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    # x,y,z = sorted((x,y,z))
    print(x, y, z)

if __name__ == '__main__':
    words_sort()
