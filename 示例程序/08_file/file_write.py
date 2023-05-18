#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def write_file(file='sample.txt'):
    f = open(file, 'w')
    print('encoding:%s' % f.encoding)
    s1='1\tfudan\t复旦大学\t中国上海\t200433\n'
    s2='2\tsjtu\t交通大学\t中国上海\t200240\n'
    f.write(s1)
    f.write(s2)
    f.close()

def write_file_2(file='sample.txt'):
    s1='11\tfudan\t复旦大学\t中国上海\t200433\n'
    s2='12\tsjtu\t交通大学\t中国上海\t200240\n'
    with open('sample.txt', 'w') as f:
      f.write(s1)
      f.write(s2)


def write_file_writelines(file='sample.txt'):
    s = ['21\tfudan\t复旦大学\t中国上海\t200433\n',
         '22\tsjtu\t交通大学\t中国上海\t200240\n',
         '23\tlast line']
    with open(file, 'a+') as f:
        f.writelines(s)
        f.seek(0)
        print(f.read())


def write_lines(lines):
    for line in lines:
        f.write(line)

def read_file(text='sample.txt'):
    with open(text, 'r') as file:
        print(file.read())

if __name__ == '__main__':
#    write_file()
    write_file_2()
    write_file_writelines()
#     read_file()
