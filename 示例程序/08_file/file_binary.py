#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def write_binary_file(file='sample.dat'):
    f = open(file, 'wb')
    chars = bytes(range(256))
    f.write(chars)
    chars = bytes(range(255, -1, -1))
    f.write(chars)
    f.close()

def read_binary_file(file='sample.dat'):
    f = open(file, 'rb')
    s = f.read()
    f.close()
    print(s)


def read_binary_file2(file='sample.dat'):
    with open(file, 'rb') as f:
        s = f.read()
    print(s)


def writelines(f, seq):
    for line in seq:
        f.write(line)

import random
def seek_file(file='sample.dat'):
    with open(file, 'rb') as f:
        f.seek(0, 2)
        size = f.tell()
        print('len:', size)
        offset = random.randint(0, size - 4)
        f.seek(offset, 0)
        print(f.read())


if __name__ == '__main__':
    write_binary_file()
    read_binary_file()
    seek_file()
