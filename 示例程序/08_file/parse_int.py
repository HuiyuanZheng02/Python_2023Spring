#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import sys
import random

def setup():
    ''' 创建两个文件，一个第一行为整数，另一个第一行为非整数'''
    with open('sample.txt', 'w') as f:
        f.write(str(random.randint(1,100)))

    with open('sample1.txt', 'w') as f:
        f.write('abc')

    with open('sample2.txt', 'w', encoding='utf-8') as f:
        f.write('中文')


def parse_int(file='sample.txt'):
    try:
        f = open(file)
        s = f.readline()   # 如果这一行执行时出错怎么办
        f.close()
        i = int(s.strip())
        print(i)
    except (OSError, ValueError) as inst:
        print(type(inst),inst)


def parse_int2(file='sample.txt'):
    try:
        f = open(file)
        s = f.readline()
        # f.close()
        i = int(s.strip())
        print(i)
    except (OSError, ValueError) as inst:
        print(type(inst),inst)
    finally:
        f.close()

def parse_int3(file='sample.txt'):
    f = None
    try:
        f = open(file)
        s = f.readline()
        # f.close()
        i = int(s.strip())
        print(i)
    except (OSError, ValueError) as inst:
        print(type(inst),inst)
    finally:
        if f:
            f.close()


def parse_int4(file='sample.txt'):
    try:
        f = open(file)
        s = f.readline()
        # f.close()
        i = int(s.strip())
        print(i)
    except (OSError, ValueError) as inst:
        print(type(inst),inst)
    finally:
        if 'f' in locals():
            f.close()

def parse_int5(file='sample.txt'):
    try:
        with open(file) as f:
            s = f.readline()
            i = int(s.strip())
            print(i)
    except (OSError, ValueError) as inst:
        print(type(inst),inst)


def test_parse():
    parse_int3('sample.txt')
    parse_int3('sample1.txt')
    parse_int3('sample2.txt')
    parse_int3('sample3.txt')

if __name__ == '__main__':
    setup()
    test_parse()
