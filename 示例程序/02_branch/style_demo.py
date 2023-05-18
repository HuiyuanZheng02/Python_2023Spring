#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
a,b, c = 3, 4, 5
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
        print('hello')        
else:
    if b > c:
        print(b)
    else:
        print(c)
        print('ok')
        
if a > b and a > c and a > 5 and b > 5 and c > 5  \
   and b > c:
    print('blah')

if (a > b and a > c and a > 5 and b > 5 and c > 5
   and b > c):
    print('blah')


def tt2(arg1, arg2,
        arg3, arg4):
    """function tt2
    arg1: xxxxx
    arg2: xxxx
    .....
    """

    print('Hello', arg1, arg2, arg3, arg4)   

def f(a=3):
    pass

f(a=4)

def isclosed(self):
    """True if the connection is closed."""
    return self.fp is None


def func(a, b, c, x='x', y='y'):
    print(a, b, c, x, y)

func(1, 2, 3, y=5)

x = 3
a = 4 + 5
x = x*2 - 1
hypot2 = x*x + y*y  # +优先级更低
c = (a+b) * (a-b)   # *相比括号优先级更低

