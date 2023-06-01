#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import re

def re_search_all():
    regexp = re.compile('((jump)ed for) (food)')
    text='The quick brown fox jumped for food. The lazy black dog jumped for food.'
    pos = count = 0
    while True:
        match = regexp.search(text, pos)
        if not match:
            break
        count += 1
        print('{} found "{}" at [{},{})'.format(count, match.group(), *match.span()))
        # print('%s found "%s" at [%s,%s]' % (count, match.group(), match.start(), match.end()))
        for k, v in enumerate(match.groups(), 1):
            print('  group %d: %s, span %s' % (k, v, match.span(k)))

        pos = match.end()

def re_finditer():
    regexp = re.compile('((jump)ed for) (food)')
    text = 'The quick brown fox jumped for food. The lazy black dog jumped for food.'
    matches_iter = regexp.finditer(text)  # iterable( matchobj1, matchobj2, ...)
    for count, match in enumerate(matches_iter, 1):  # iterable: (1, matchobj1), (2,matchobj2)...
        print('{} found "{}" at [{},{})'.format(count, match.group(), *match.span()))
        # print('%s found "%s" at [%s,%s]' % (count, match.group(), match.start(), match.end()))
        for k, v in enumerate(match.groups(), 1):
            print('  group %d: %s, span %s' % (k, v, match.span(k)))

def re_findall():
    text='The quick brown fox jumped for food. The lazy black dog jumped for food.'

    print(re.findall('jumped for food', text)) #没有group，包含匹配的模式
    print(re.findall('jumped for (food)', text))
    print(re.findall('(((jump)ed for) (food))', text)) #4个group，group 1包含所有内容

def re_escape_test():
    """ \后面跟着英文字母、数字和标点符号时正则表达式是否合法 """
    import string
    text = 'abcdefg'
    valids = string.ascii_letters + string.digits + string.punctuation
    for ch in valids:
        pattern = '\\' + ch
        try:
            regexp = re.compile(pattern)
            if not regexp.search(text):
                print('re %s not match  %s' % (pattern, pattern))
        except Exception as e:
            print(pattern, e)

def re_escape(name='(food)'):
    """ 搜索当前文件中出现的name
    """
    cre = re.compile(re.escape(name))
    print(cre.pattern)
    with open(__file__, encoding='utf-8') as f:
        text = f.read()
        lineno = 1
        pos = 0
        for match in cre.finditer(text):
            lineno += text[pos:match.end()].count('\n')
            pos = match.end()
            print('[line %d] found %s ' % (lineno, match.group()))


def re_escape2():
    text = """regexp = re.compile('((jump)ed for) (food)')
    text='The quick brown fox jumped for food. The lazy black dog jumped for food.'
    print(regexp.findall(text))

    regexp2 = re.compile('(((jump)ed for) (food))')
    print(regexp2.findall(text))

    regexp3 = re.compile('jumped for food')
    print(regexp3.findall(text))

    """
    pattern = input("请输入要匹配的内容:")
    esc_pattern = re.escape(pattern)
    print('正则表达式为', esc_pattern)
    matches = re.findall(esc_pattern, text)
    print(matches)


if __name__ == '__main__':
    re_search_all()
    print('-' * 30 + 're_finditer' + '-' * 30 )
    re_finditer()
    print('-' * 30 + 're_findall' + '-' * 30 )
    re_findall()
    print('-' * 30 + 're_escape' + '-' * 30 )
    re_escape()
