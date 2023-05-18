#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

'''
某些字符转换为大写：
实现函数 upper_for_chars(text, toUpper)，将text中的toUpper中的那些字符变为大写，返回新的字符串
    # upper_for_chars('Hello world', 'aeiouy') 返回 HEllO wOrld
'''

def upper_for_chars(text, toUpper):
    # upper_for_chars('Hello world', 'aeiouy')  --》 'HEllO wOrld'
    return text


def test():
    print(upper_for_chars('Hello world', 'aeiouy'))

if __name__ == '__main__':
    test()
