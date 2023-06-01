#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import re


text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''

def re_sub_string():
    # 将以字母“b”和”B”开头的单词替换为“*”
    pattern = r'\b[bB]\w*\b'
    print(re.sub(pattern, '*', text))

    print()
    # 将第一个以字母“b”和”B”开头的单词替换为“*”
    print(re.sub(pattern,'*',text, 1))

    print()
    # 将以字母“b”和”B”开头的单词前面添加*
    pattern = r'\b([bB]\w*)\b'
#    print(re.sub(pattern, r'*\1', text))
    print(re.sub(pattern, r'*\g<1>', text))

def re_sub_func():
    # Complex is better than complicated.
    pattern = r'\b([BC]\w*)\b\s+is\s+(better|worse)\s+than\s+(\w+)\b'
    # print(re.findall(pattern, text))

    def repl_func(match):
        first = match.group(1)
        last = match.group(3)
        return '%s is %s than %s' %   (last.capitalize(),
                'worse' if match.group(2) == 'better' else 'better',  first.lower())

    text_ = re.sub(pattern, repl_func, text)
    print()
    print(text_)

if __name__ == '__main__':
    re_sub_string()
    re_sub_func()
