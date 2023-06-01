#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def is_valid_email(email):
    """
    RFC 5322 Section 3.4.1给出了电子邮件地址的格式
    local-part@domain
    local-part和domain部分的定义一致，由一个或多个部分组成，这些部分之间以点隔开。每个部分允许是英文字母、数字、下划线以及下述特殊字符
    special = "{}+-*/%=|?^$!&#'`~"
    """
    special = "{}+-*/%=|?^$!&#'`~"
    return False


text = '<a href="index.htm">Welcome to Fudan University!</a>'

def get_text(href_text=text):
    """
    '<a href="index.htm">Welcome to Fudan University!</a>'
    返回 Welcome to Fudan University!
    """
