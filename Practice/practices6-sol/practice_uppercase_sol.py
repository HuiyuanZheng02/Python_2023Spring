#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


'''
某些字符转换为大写：

实现函数 upper_for_chars(text, toUpper)，将text中的toUpper中的那些字符变为大写，返回新的字符串
    # upper_for_chars('Hello world', 'aeiouy') 返回 HEllO wOrld
'''

def upper_for_chars(text, toUpper):
    # upper_for_chars('Hello world', 'aeiouy')  --》 'HEllO wOrld'
    pass
    upper_map = str.maketrans(toUpper, toUpper.upper())
    return text.translate(upper_map)

def upper_for_chars2(text, toUpper):
    # upper_for_chars2('Hello world', 'aeiouy')
    pass
    return ''.join([c.upper() if c in toUpper else c for c in text])

def upper_for_chars3(text, toUpper):
    # upper_for_chars3('Hello world', 'aeiouy')
    result = []
    for ch in text:
        if ch in toUpper:
            ch = ch.upper()
        result.append(ch)
    return ''.join(result)


def test():
    func_lists = upper_for_chars, upper_for_chars2, upper_for_chars3
    for func in func_lists:
        print(func('Hello world', 'aeiouy'))


if __name__ == '__main__':
    test()