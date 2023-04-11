#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def f0(iterable):
    s = []
    for item in iterable:
        s.append(item ** 2)
    return s

def f(iterable):
    for item in iterable:
        yield item ** 2

g = f(range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))

print(list(f(range(10))))

def f1():
    yield from 'welcome to the python world.'

def f2():
    for i in 'welcome to the python world.':
        yield i

def count(start=0, step=1):
    while True:
        yield start
        start += step

for i in count():
    if i % 10 == 0:
        print(i)
    if i > 100:
        break

import random
def producer():
    while True:
        value = random.randint(0, 100)
        print('\n[PRODUCER]: produce', value)
        try:
            feedback = yield value
            print('[PRODUCER]: got feedback', feedback)
        except GeneratorExit:
            print('[PRODUCER]: done')
            break
        except Exception as e:
            print('[PRODUCER]: caught exception', type(e), e)

def consumer(p):
    value = p.send(None)
    for i in range(5):
        print('[CONSUMER]: got ', value)
        feedback = '奇数' if value % 2 else '偶数'
        value = p.send(feedback)

    print('[CONSUMER]: got ', value)
    value = p.throw(TypeError, 'spam')
    print('[CONSUMER]: got ', value)
    p.close()    

def test_generator_function():
    p = producer()
    consumer(p)

test_generator_function()
