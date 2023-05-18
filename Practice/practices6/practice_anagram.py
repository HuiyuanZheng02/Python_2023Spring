#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def is_anagram(word1, word2):
    """ 检查两个单词是否为相似词。两个单词如果包含相同的字母，
    则它们是相似词。例如：silent和listen是相似词。.
    """
    return True


def test_anagram():
    test_cases = ('listen','silent', True), ('banana', 'anbaan', True), ('listen', 'silenta', False)
    for text1, text2, result in test_cases:
        if is_anagram(text1, text2) == result:
            print('%s and %s are %sanagrams' % (text1, text2, '' if result else 'not '))
        else:
            print('anagram(%s, %s) returns %s, expecting %s' % (text1, text2, not result, result))

if __name__ == '__main__':
    test_anagram()