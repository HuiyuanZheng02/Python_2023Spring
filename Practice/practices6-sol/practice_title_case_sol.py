#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


"""
练习题 2：
实现 my_capitalize(text): 首字母大写，其他字母小写
实现 my_title(text): 每个单词首字母大写，其他字母小写
#  text = 'What is YoUr NaMe?'
"""

def my_capitalize(text):
    # 首字母大写，其他字母小写
    # my_capitalize('What is YoUr NaMe?')

    lc_text = text.lower()
    return lc_text[0].upper() + lc_text[1:]

def my_title(text):
    '''每个单词首字母大写，其他字母小写 '''
    # my_title('What is YoUr NaMe?')

    return ' '.join(token.capitalize() for token in text.split())


if __name__ == '__main__':
    text = 'What is YoUr NaMe?'
    cap_text = my_capitalize(text)
    print('Capitalized text:', cap_text)

    title_text = my_title(text)
    print('Titled text:', title_text)
