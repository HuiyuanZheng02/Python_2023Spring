#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import re

pattern1 = r'((\d{2})-)?(\d{2,3})-(\d{7,8})'
text1 = 'Tel: 86-21-65642222,'
text2 = 'Tel: 21-65642222,'
print('-' * 30, 'pattern=%s' % pattern1, '-' * 30)
for text in (text1, text2):
    print('-' * 40)
    match = re.search(pattern1, text)
    print(match)
    print(match.groups())
    print('match: %s, span %s' % (match.group(), match.span()))
    for k, v in enumerate(match.groups(), 1):
        print('group %d: %s, span %s' % (k, v, match.span(k)))


pattern2 = r'(?:(\d{2})-)?(\d{2,3})-(\d{7,8})'
print('-' * 30, 'pattern=%s' % pattern2, '-' * 30)
for text in (text1, text2):
    match = re.search(pattern2, text)
    print(match)
    print(match.groups())
    print('match: %s, span %s' % (match.group(), match.span()))
    for k, v in enumerate(match.groups(), 1):
        print('group %d: %s, span %s' % (k, v, match.span(k)))

pattern3 = r'((?P<country>\d{2})-)?(?P<city>\d{2,3})-(?P<phone>\d{7,8})'
print('-' * 30, 'pattern=%s' % pattern3, '-' * 30)
for text in (text1, text2):
    match = re.search(pattern3, text)
    print(match)
    print(match.groups())
    print('match: %s, span %s' % (match.group(), match.span()))
    for k, v in enumerate(match.groups(), 1):
        print('group %d: %s, span %s' % (k, v, match.span(k)))

    print(match.groupdict())

pattern3 = r'(?:(?P<country>\d{2})-)?(?P<city>\d{2,3})-(?P<phone>\d{7,8})'
print('-' * 30, 'pattern=%s' % pattern3, '-' * 30)
for text in (text1, text2):
    match = re.search(pattern3, text)
    print(match)
    print(match.groups())
    print('match: %s, span %s' % (match.group(), match.span()))
    for k, v in enumerate(match.groups(), 1):
        print('group %d: %s, span %s' % (k, v, match.span(k)))

    print(match.groupdict())


def re_back_reference():
    pattern = r'(\b\w+)\s+\1'
    match = re.search(pattern,'Paris in the the spring')
    print('group 0:(%s) group 1:(%s)' % (match.group(), match.group(1)))

    pattern = r'((\b\w+)\s+\2)'
    print(re.findall(pattern, 'Paris in the the spring'))

    pattern = r'(?P<word>\b\w+)\s+(?P=word)'
    match = re.search(pattern,'Paris in the the spring')
    print('group word:', match.group('word'))
    print(match.group())

def re_select():
    text = 'ch4/re_usage.py ch4/re select.py ch4/readme.txt ch4/readme.md ch4/re.pdf ch3/loop.py'
    matches = re.findall(r'(ch\d/\w+\.(py|txt))', text)
    matches = [item[0] for item in matches]
    print(matches)
    # ['ch4/re_usage.py', 'ch4/readme.txt', 'ch3/loop.py']

    pattern =  r'(ch\d/[^.]+\.(py|txt))'
    matches = re.findall(pattern, text)
    matches = [item[0] for item in matches]
    print(matches)


def re_flag():
    text = '''# -*- coding: utf-8 -*-
import math
from os import *
print('test')
'''
    match = re.search(r'^.+\*$', text)
    if match:
        print(match.re)
        print(match.group())

    match = re.search(r'^.+\*$', text, re.M)
    if match:
        print(match.re)
        print(match.group())

if __name__ == '__main__':
    pass
    re_flag()
