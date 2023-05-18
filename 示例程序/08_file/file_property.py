#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def print_file_property(file='sample.txt'):
    fh = open(file)
    print('file name  : %s' % fh.name)
    print('access mode: %s' % fh.mode)
    print('encoding   : %s' % fh.encoding)
    print('closed     : %s' % fh.closed)
    fh.close()

def setup(file='sample.txt'):
    import os.path
    if not os.path.exists(file):
        fh = open(file, 'w')
        fh.write('1  python程序设计\n2 C程序设计\n')
        fh.close()


if __name__ == '__main__':
    setup()
    print_file_property()
#    input()
