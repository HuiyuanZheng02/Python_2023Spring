#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def is_anagram(word1, word2):
    """ 检查两个单词是否为相似词。两个单词如果包含相同的字母，
    则它们是相似词。例如：silent和listen是相似词。.
    """
    if  len(word1) != len(word2):
        return False
    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            return False
    return True

def is_anagram2(word1, word2):
    """ 检查两个单词是否为相似词。两个单词如果包含相同的字母，
    则它们是相似词。例如：silent和listen是相似词。.
    """
    if  len(word1) != len(word2):
        return False
    list1 = sorted(word1)
    list2 = sorted(word2)
    return list1 == list2


def is_anagram3(word1, word2):
    """ 检查两个单词是否为相似词。两个单词如果包含相同的字母，
    则它们是相似词。例如：silent和listen是相似词。.
    """
    if  len(word1) != len(word2):
        return False
    d1 = {}
    for ch in word1:
        d1[ch] = d1.get(ch, 0) + 1

    d2 = {}
    for ch in word2:
        d2[ch] = d2.get(ch, 0) + 1
    return d1 == d2


def test_anagram():
    test_cases = ('listen','silent', True), ('banana', 'anbaan', True), ('listen', 'silenta', False)
    for text1, text2, result in test_cases:
        if is_anagram3(text1, text2) == result:
            print('%s and %s are %sanagrams' % (text1, text2, '' if result else 'not '))
        else:
            print('anagram(%s, %s) returns %s, expecting %s' % (text1, text2, not result, result))

if __name__ == '__main__':
    test_anagram()
