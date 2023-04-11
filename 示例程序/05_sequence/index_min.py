#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import random

def index_min(s):
    min_value = min(s)
    result = (min_value, )
    for index, value in enumerate(s):
        if value == min_value:
            result = result + (index,)
    return result



def index_min2(s):
    min_value = min(s)
    result = [min_value]
    for index, value in enumerate(s):
        if value == min_value:
            result.append(index)
    return tuple(result)


if __name__ == '__main__':
    x = [random.randint(1, 20) for i in range(50)]
    print(x)
    print(index_min(x))
    print(index_min2(x))
