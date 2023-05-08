#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import sys

def _print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    line = []
    for value in args:
        line.append(format(value))
    file.write(sep.join(line))
    file.write(end)
    if flush:
        file.flush()


if __name__ == '__main__':
    _print(1, 2, 3, sep='*', end='=')
    _print(1 * 2 * 3)
