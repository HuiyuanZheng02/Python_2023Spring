#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import re

text = '''
  abc  2016-10-31
   xyz   2016-9-4
   aef   2016-10-aa
    asasf asdf 10-14
  2013-10-3  234234
  1945-8-15 abc  1945
  1972-01-30 asdf  1988-10-1
'''

'''
 字符串text里面包含了多个日期，将文本里面出现的合法日期转换格式，如
 2016-10-31  -->  10/31/2016
 2016-9-4    -->  09/04/2016
 最后输出转换后的日期

 1. 10/31/2016
 2. 09/04/2016
 3. 10/03/2013
 4. 08/15/1945
 5. 01/30/1972
 6. 10/01/1988
 '''

def format_date():
    pattern = r'\b(\d{4})-(\d{1,2})-(\d{1,2})\b'
    # 2016-10-31
    match_iter = re.finditer(pattern, text)
    date_lists = []
    for match in match_iter:
        year, month, day = match.groups()
        month = '0' + month if len(month) == 1 else month
        day = '0' + day if len(day) == 1 else day
        # '{:>02}'.format(month)
        # '%02' % month
        date_lists.append('/'.join((month, day, year)))

    for k, v in enumerate(date_lists, 1):
        print('%d. %s' % (k, v))

def format_date2():
    pattern = r'\b(\d{4})-(\d{1,2})-(\d{1,2})\b'
    # 2016-10-31
    matches = re.findall(pattern, text)
    date_lists = []
    for year, month, day in matches:
        month = '0' + month if len(month) == 1 else month
        day = '0' + day if len(day) == 1 else day
        # '{:>02}'.format(month)
        # '%02' % month
        date_lists.append('/'.join((month, day, year)))

    for k, v in enumerate(date_lists, 1):
        print('%d. %s' % (k, v))

if __name__ == '__main__':
    format_date()
    print()
    format_date2()
