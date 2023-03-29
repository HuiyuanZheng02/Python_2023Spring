#! /usr/bin/env python3
'''模块文档字符串__doc__:第一个语句为字符串表达式时'''

import math

def distance(x1, y1, x2, y2):
    """返回两点间的距离
    传递的参数为第一个点的X轴和Y轴坐标，第二个点的X轴和Y轴坐标
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    dist = distance(0,0, 4.5, 4.5)
    print('(0,0)与(4.5,4.5)间的距离为', round(dist, 2))
