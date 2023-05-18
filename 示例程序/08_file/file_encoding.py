#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def read_file_read(file='sample.txt'):
    with open(file, 'r') as f:
        text = f.read()
    print('-'*40)
    print(text)


def read_python_file(file=None, encoding=None):
    """ 打开文件时，缺省编码方式为locale.getpreferredencoding()返回的编码,
    而python源程序缺省编码为UTF-8，如果其中有中文时就会出现问题。
    """
    if not file:
        file = __file__
        encoding = encoding or 'utf-8'

    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    print(text)


if __name__ == '__main__':
    try:
        read_file_read(__file__)
    except Exception as e:
        print('Exception %s raised... %s' % (type(e), e))

    print('-' * 20, 'read_python_file', '-' * 20)
    read_python_file()
