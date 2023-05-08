#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def kwonly(a, *b, c, d=5):
    return (a,b,c,d)

def kwonly2(a, b, *, c, d=5):
    return (a,b,c,d)

print(kwonly(1, 2, c=3))
print(kwonly(1, 2, c=3, d=4))

print(kwonly2(1, 2, c=3))
print(kwonly2(1, 2, c=3, d=4))


if __name__ == '__main__':
    pass