#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import random

def test_dict():
    name = 'tony'
    score = random.randint(80,99)

    d = { }

    if name in d:
        d[name].append(score)
    else:
        d[name] = [score]
    print(d)

    score = random.randint(80,99)

    d[name] = d.get(name, [])
    d[name].append(score)
    print(d)

    d1_err = { }
    d1_err[name] = d1_err.get(name, []).append(score)
    print(d1_err)

    score = random.randint(80,99)
    d[name] = d.get(name, []) + [score]
    print(d)

    d.setdefault(name,[]).append(score)
    print(d)

    from collections import defaultdict
    d5 = defaultdict(list)
    d5[name].append(score)
    print(d5)

if __name__ == '__main__':
    test_dict()
