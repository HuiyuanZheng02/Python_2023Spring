#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import sys

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

def test_divide():
    divide(2, 1)
    print()
    
    divide(2, 0)
    print()
    
    divide("2", "1")
    print('done...')

def demo_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("division by zero!")
        # return 0
    finally:
        print('finally')
        return -1   

def test_div():
    print(demo_div(1, 2))
    print()
    
    print(demo_div(1, 0))

if __name__ == '__main__':
    # test_divide()
    try:
        test_div()
    except Exception as e:
        print(type(e), e)
        
