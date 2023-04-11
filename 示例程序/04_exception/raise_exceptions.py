#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import logging
logging.basicConfig(filename='main.log',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.DEBUG)
logging.info('logging started.')

def my_find(text, pattern):
    try:
        return text.index(pattern)
    except IndexError:
        return -1

def my_index(text, pattern):
    idx = text.find(pattern)
    if idx != -1:
        return idx
    raise IndexError(pattern + 'not found')


def my_find2(text, pattern):
    if pattern in text:
        return text.index(pattern)
    return -1

def compute_circle_area(radius):
    if not isinstance(radius, (float, int)) or radius < 0:
        raise ValueError('radius should be a number larger than 0')
    return math.pi * radius * radius


def get_threshold(prompt=None) :
    try:
        thresh = int(input(prompt))
        return thresh
    except ValueError as e:
#        print(type(e), e)
        logging.error('get_threshold failed')
        logging.exception(e)
        raise


if __name__ == '__main__':
    get_threshold('threshold=')
