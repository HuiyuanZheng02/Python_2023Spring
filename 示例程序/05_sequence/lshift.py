#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def lshift0(s, k):
    x = s[:k]
    x.reverse()
    y = s[k:]
    y.reverse()
    r = x + y
    r.reverse()
    return r

def lshift(s, k):
    s[:k] = reversed(s[:k])
    s[k:] = reversed(s[k:])
    s.reverse()

def lshift2(s, k):
    s[:k] = s[k-1::-1]
    s[k:] = s[:k-1:-1]
    s.reverse()

if __name__ == '__main__':
    s = list(range(1, 21))
    s2 = s[:]
    print(s)
    print(lshift0(s, 5))
    lshift(s, 5)
    print(s)
    lshift2(s2, 5)
    print(s2)
