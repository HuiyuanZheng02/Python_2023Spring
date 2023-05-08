#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def test_letter_counter():
    import string
    import random
    x = string.ascii_letters + string.digits + string.punctuation
    y = [random.choice(x) for i in range(1000)]
    z = ''.join(y)
    print('测试字符串...')
    print(z)

    counters = letter_counter(z)
    print('统计结果为:',counters)
    for letter in counters:
        print('%c 的出现次数==> %d' % (letter, counters[letter]))

    print()
    counters2 = letter_counter2(z)
    print('统计结果为:',counters2)
    for letter in counters2:
        print('%c 的出现次数==> %d' % (letter, counters2[letter]))

    print()
    counters3 = letter_counter3(z)
    print('统计结果为:',counters3)
    for letter in counters3:
        print('%c 的出现次数==> %d' % (letter, counters3[letter]))

def letter_counter(seq):
    counters = dict()
    for item in seq:
        counters[item] = counters.get(item, 0) + 1
    return counters

def letter_counter2(seq):
    from collections import defaultdict
    counters = defaultdict(int)
    for item in seq:
        counters[item] += 1
    return counters

def letter_counter3(seq):
    from collections import Counter
    return Counter(seq)

if __name__ == '__main__':
    test_letter_counter()
