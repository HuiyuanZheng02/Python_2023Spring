#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def demo(*para):
    avg = sum(para) / len(para)
    g = [i for i in para if i > avg]
#    return (avg, *g)
    return (avg,) + tuple(g)


if __name__ == '__main__':
    print(demo(1, 2, 3, 4))
