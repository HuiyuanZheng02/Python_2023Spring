#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def yanghui_triangle(n):
    print([1])    # 第一行
    print([1, 1]) # 第二行
    line = [1, 1] # line纪录上一行的内容
    for i in range(2, t): # 从第3行开始，每次输出一行
        r = []
        # 根据上一行计算下一行中间部分的内容
        for j in range(0, len(line) - 1):
            r.append(line[j] + line[j + 1])
        line = [1] + r + [1]
        print(line)


def yanghui_triangle(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError('A positive integer is expected.') 
    triangle = [[1]]
    if n == 1:
        return triangle
    line = []
    for i in range(1, n):
        new_line = [1]
        for j in range(0, len(line) - 1):
            new_line.append(line[j] + line[j + 1])
        new_line.append(1)
        triangle.append(new_line)
        line = new_line
    return triangle



def c():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

def yanghui_triangle2(t):
    g = yanghui_triangle2(10)()
    for n in range(t):
        print(next(g))


if __name__ == '__main__':
    matrix = yanghui_triangle(10)
    import pprint
    pprint.pprint(matrix)
    yanghui_triangle2(10)

