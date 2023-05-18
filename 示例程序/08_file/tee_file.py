#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def setup():
    ''' 创建一个文件'''
    with open('sample.txt', 'w') as f:
        f.writelines(['1 how are you?\n', '2 fine, thank you\n', '3 what about you?\n'])

def tee(in_file, out_file1, out_file2):
    with (open(in_file, 'rb') as file,
          open(out_file1, 'wb') as file1,
          open(out_file2, 'wb') as file2):
        text = file.read()
        file1.write(text)
        file2.write(text)

if __name__ == '__main__':
    setup()
    print('-' * 40)
    tee('sample.txt', 'sample.1.txt', 'sample.2.txt')
