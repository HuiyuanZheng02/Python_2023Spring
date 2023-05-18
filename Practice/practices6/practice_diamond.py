#!/usr/bin/env python3
#  -*- coding: utf-8 -*-



'''
用户输入一个正整数n，输出一个菱形
    n = 5 :
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *

'''

def diamond_n(n):
    """ 输入任意一个正整数，显示相应大小的菱形。
    n = 5 :
              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
    * * * * * * * * * * *
      * * * * * * * * *
        * * * * * * *
          * * * * *
            * * *
              *

    """
    pass


def test_diamond():
    n = int(input('Please input n='))
    diamond_n(n)


if __name__ == '__main__':
    test_diamond()