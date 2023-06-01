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
    print()
    # 菱形：上部份n行，中间一行包括 2n+1个star，中间添加 2n个space
    for i in range(n):
        # 第i in [0,n) 行: 每行*个数为 2*i+1
        stars = ' '.join('*' * (2 * i + 1))
        # 2*n + 1 * , 2n space, 居中对齐，不够用空格填充
        line = stars.center(2 * n + 1 + 2 * n, ' ')
        print(line)

    # 下半部分i从n-->0
    for i in range(n, -1, -1):
        stars = ' '.join('*' * (2 * i + 1))
        line = stars.center(2 * n + 1 + 2 * n, ' ')
        print(line)

def test_diamond():
    n = int(input('Please input n='))
    diamond_n(n)


if __name__ == '__main__':
    test_diamond()