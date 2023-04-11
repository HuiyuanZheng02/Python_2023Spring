#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def gcd(m, n):
    if m > n:
        m, n = n, m
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    return (int(p / n), n)

def gcd(m, n):
    p = m * n
    while m != 0:
        m,n = n % m, m
    return (n, p // n)


if __name__ == '__main__':
    print(gcd(20, 30))
    print(gcd(30, 20))
