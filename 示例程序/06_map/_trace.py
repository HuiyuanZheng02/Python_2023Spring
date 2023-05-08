#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def _trace(func,*args,**kwargs):
    if hasattr(func,'calls'):
        func.calls += 1
    else:
        func.calls = 1
    if kwargs:
        print('[%d] calling function: %s(%s,%s)'% (func.calls,
                func.__name__, ','.join([str(item) for item in args]), ','.join([k+'='+str(v) for k,v in kwargs.items()])))
    else:
        print('[%d] calling function: %s(%s)'% (func.calls,
                func.__name__, ','.join([str(item) for item in args])))
    return func(*args,**kwargs)

def demo(a,b=4,*x, **y):
    print(a, b, x, y)

if __name__ == '__main__':
    _trace(demo, 1)
    _trace(demo, 1, 2)
    _trace(demo, 1, 2, 3, 4, c=9, d=8)
