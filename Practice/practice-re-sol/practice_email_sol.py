#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import re

def is_valid_email(email):
    """
    RFC 5322 Section 3.4.1给出了电子邮件地址的格式
    local-part@domain
    local-part和domain部分的定义一致，其由一个或多个部分组成，这些部分之间以点隔开。每个部分允许是英文字母、数字、下划线以及下述特殊字符
    special = "{}+-*/%=|?^$!&#'`~"
    """
    # name1.name2.name3.name@dn1.dn2.dn3.dn1
    # (((name1\.){0,}\.name)@....)
    # [\d\w]
    special = "{}+-*/%=|?^$!&#'`~"
    special2 = "{}+*/%=|?^$!&#'`~-"
    pattern = r'(([\w\d{special}]+\.)*([\w\d{special}]+))@(([\w\d{special}]+\.)*([\w\d{special}]+))\b'.format(
        special=special2)
    # print(pattern)
    # return re.fullmatch(pattern, email) != None
    match = re.fullmatch(pattern, email)
    if match == None:
        return False
    # print(match.group(), match.group(1), match.group(4))
    return True


text = '<a href="index.htm">Welcome to Fudan University!</a>'

def get_text(href_text=text):
    """
    '<a href="index.htm">Welcome to Fudan University!</a>'
    返回 Welcome to Fudan University!
    """

    pattern = r'<a\s+href=".+?"\s*>\s*(.+?)\s*</a>'
    matches = re.findall(pattern, text)
    if not matches:
        print('No match!')
        return []
    for item in matches:
        print(item)
    return matches

if __name__ == '__main__':
    emails = 'foo@www', 'alice.wang@gmail.com', 'alice@gmail..com', 'hello', 'cs&fudan.edu.cn', 'sally.phillips+unique_reference@gmail.com'
    for addr in emails:
        ret = is_valid_email(addr)
        print('{}...{}'.format(addr, ret))

    ret = get_text(text)
    print(ret)
