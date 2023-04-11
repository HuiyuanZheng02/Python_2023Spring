#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def assert_divzero( ):
    a = int(input('请输入被除数:'))
    b = int(input('请输入除数:'))
    assert b!=0, '除数不能为0!'
    c = a/b
    print(a,'/',b,'=',c)


if __name__ == '__main__':
    assert_divzero()