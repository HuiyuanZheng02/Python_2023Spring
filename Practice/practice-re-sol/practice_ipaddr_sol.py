#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
text中有多个IP地址，每个IP地址包含了4个（1到3位）正整数，这些整数之间以点分割。
请输出其中包含的所有IP地址
"""

import re

# ((\d{1,3}\.){3}\d{1,3})


text = r"""127.0.0.1   localhost
  202.120.224.10   mail.fudan.edu.cn
    202.120.225.10   www.fudan.edu.cn
8.8.8.8   dns.gooogle.com
61.135.169.121 www.baidu.com
"""

pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ipaddr_list = []
for match in re.finditer(pattern, text, re.A):
    ipaddr_list.append(match.group())

print('\n'.join(ipaddr_list))

print()
ipaddr_list = re.findall(pattern, text, re.A)
print('\n'.join(ipaddr_list))

print()
pattern2 = r'((\d{1,3}\.){3}\d{1,3})'
matches = re.findall(pattern2, text, re.A)
ipaddr_list = [ip for ip, x in matches]
print('\n'.join(ipaddr_list))

if __name__ == '__main__':
    pass
