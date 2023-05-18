#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def setup(file='sample.txt'):
    import os.path
    with open(file, 'w') as f:
        f.write('1 python程序设计\n2 C程序设计\n3 VB')

def read_file_read(file='sample.txt'):
    with open(file, 'r') as f:
        print('encoding:', f.encoding)
        firstN = f.read(10)
        print('current offset:', f.tell())
        f.seek(0)
        lines = f.read()
    print('first 10 chars:\n%s' % firstN)
    print('-'*40)
    print(lines)

def read_file_readline(file='sample.txt'):
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line,end='')

    f.close()

def read_file_readlines(file='sample.txt'):
    with open(file, 'r') as f:
        lines = f.readlines()
    print(lines)
    print()
    for line in lines:
        print(line,end='')


def seek_file(file='sample.txt'):
    """ 演示读写模式以及seek/tell用法
    """
    with open(file, 'r+') as f:
        f.seek(0, 2)  # 移动到文件结尾
        f.write('程序设计\n')
        pos = f.tell()
        f.write('4 Java程序语言')
        f.seek(pos)
        f.write('4 Java程序设计')

    print()
    with open(file) as f:
        print(f.read())


def read_file_iterator(file='sample.txt'):
    with open(file,'r') as f:
        for line in f:
            print(line,end='')


def read_file_list_comprehension(name='sample.txt', num=-1):
    file = open(name,'r')
    if num < 0:
        lines = [line for line in file]
    else:
        lines = []
        for i in range(num) : #
            lines.append(file.readline())

        file_iter = iter(file)  # omitted
        lines = [next(file_iter) for i in range(num) ]

        # iterable   0     1 ,      N-1
        # list       line1, line2, ... lineN
    file.close()
    print(lines)
    return lines

if __name__ == '__main__':
    setup()

    print('-' * 20, 'read()....','-' * 20,)
    read_file_read()
    print()

    print('-' * 20, 'readline()....','-' * 20)
    read_file_readline()
    print()

    print('-' * 20, 'readlines()....','-' * 20,)
    read_file_readlines()
    print()


    print('-' * 20, 'iterator....','-' * 20,)
    read_file_iterator()
    print()

    print('-' * 20, 'list comprehension....','-' * 20,)
    read_file_list_comprehension()
    print()

    seek_file()
