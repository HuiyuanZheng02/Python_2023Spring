#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import random


def montecarlo_pi(tries=1000000):
    hits = 0
    
    for i in range(tries):
        x = random.random()*2 - 1
        y = random.random()*2 - 1

        if x*x + y*y <= 1:
            hits += 1

    pi = 4 * hits / tries

    return pi


if __name__ == '__main__':
    pi = montecarlo_pi()
    print('pi=', pi)
