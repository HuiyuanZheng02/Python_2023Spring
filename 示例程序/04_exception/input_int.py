#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def input_int():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError as e:
            print('Exception {} {}'.format(type(e), e) )
            print("That was not a valid number.  Try again...")
        except Exception as e:
            print(type(e), e)
    return x

def input_int2():
    while True:
        x = input("Please enter a number: ")
        if not x :
            continue
        if x.isdigit() or (x[0] in '+-' and x[1:].isdigit()):
            x = int(x)
            break
        print("That was not a valid number.  Try again...")

    return x

if __name__ == '__main__':
    x = input_int()
    print(x)

    print('-' * 40)
    x = input_int2()
    print(x)
