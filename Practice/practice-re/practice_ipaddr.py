#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
text中有多个IP地址，每个IP地址包含了4个（1到3位）正整数，这些整数之间以点分割。
请输出其中包含的所有IP地址，比如
127.0.0.1
202.120.224.10
202.120.225.10
8.8.8.8
61.135.169.121
"""

import re


text = r"""127.0.0.1   localhost
  202.120.224.10   mail.fudan.edu.cn
    202.120.225.10   www.fudan.edu.cn
8.8.8.8   dns.gooogle.com
61.135.169.121 www.baidu.com
"""


if __name__ == '__main__':
    pass