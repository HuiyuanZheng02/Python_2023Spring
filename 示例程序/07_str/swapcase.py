#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def swapcase(text):
    ''' swapcase('What is YoUr NaMe?')'''
    text2 = []
    for ch in text:
        if 'a' <= ch <= 'z':
            text2.append(chr(ord(ch) - ord('a') + ord('A')))
        elif 'A' <= ch <= 'Z':
            text2.append(chr(ord(ch) - ord('A') + ord('a')))
        else:
            text2.append(ch)
    return ''.join(text2)

def swapcase2(text):
    ''' swapcase2('What is YoUr NaMe?')'''
    sw_text = []
    for ch in text:
        if ch.islower():
            sw_text.append(ch.upper())
        elif ch.isupper():
            sw_text.append(ch.lower())
        else:
            sw_text.append(ch)
    return ''.join(sw_text)

if __name__ == '__main__':
    text = input('请输入一个字符串:')
    print(swapcase(text))
