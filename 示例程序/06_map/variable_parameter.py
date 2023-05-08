#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def variable_parameter(a, b=4, *x, **y):
    return (a, b, x, y)


def test_variable_parameter():
    print(variable_parameter(1))
    print(variable_parameter(1, 2))
    print(variable_parameter(1, 2, 3, 4, 5))
    print(variable_parameter(1, u=11, v=12, w=13))
    print(variable_parameter(1, 2, 3, 4, 5, u=11, v=12, w=13))

def func1(p1, p2, d1='v1', d2='v2', *var, k1, k2='kv2', **mapping):
    print(p1, p2, d1, d2, var, k1, k2, mapping)


if __name__ == '__main__':
    test_variable_parameter()

    print()
    func1(*(1, 2, 3, 4, 5, 6, 7), k1='hello k1', k3=4, k5=7)
