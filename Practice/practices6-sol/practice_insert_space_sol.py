#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def insert_spaces(word ):
   """ 用户随意输入一串字符，程序依次在相邻位置插入一个空格，逐行输出。
Universit y
Universi ty
Univers ity
Univer sity
Unive rsity
Univ ersity
Uni versity
Un iversity
U niversity
----------
U niversity
Un iversity
Uni versity
Univ ersity
Unive rsity
Univer sity
Univers ity
Universi ty
Universit y
   """
   for i in range(len(word) - 1, 0, -1):
       print(word[:i] + ' ' + word[i:])
   print('-' * len(word))
   for i in range(1, len(word)):
       print(word[:i] + ' ' + word[i:])


if __name__ == '__main__':
    text = 'University'
    insert_spaces(text)
