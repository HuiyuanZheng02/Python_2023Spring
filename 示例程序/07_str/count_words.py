#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import string
def count_words(sentence='If winter comes, can spring be far behind?'):
    #统计文章的单词个数。约定单词由英文字母组成，其他字符只是用来分隔单词。
    words = 0
    inword = False
    for c in sentence:
        if inword:
            if c not in string.ascii_letters:
                inword = False
        else:
            if c in string.ascii_letters:
                inword = True
                words += 1
    return words

"""
   If winter comes, can spring be far behind?
"""

def test_count_words():
    s = input('请输入多个英文单词，可以用任何非英文字母分割单词\n')
    words = count_words(s)
    print('英文单词个数:%d' % words)


if __name__ == '__main__':
    test_count_words()
