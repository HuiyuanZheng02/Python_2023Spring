#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from string import Formatter
import unicodedata
"""
# east_asian_width (ea)
ea ; A         ; Ambiguous    不确定
ea ; F         ; Fullwidth    全宽
ea ; H         ; Halfwidth    半宽
ea ; N         ; Neutral      中性
ea ; Na        ; Narrow       窄
ea ; W         ; Wide         宽
"""

def width_east_str(text):
    """ 返回text的占得英文字符的宽度  """
    t = [ 2 if unicodedata.east_asian_width(ch) in 'WFA' else 1 for ch in text ]
    return sum(t)

def format_east_str(text, min_width=10, justify=None, fillchar=' ' ):
    """ 格式化字符串text, 最小宽度为10，
    填充缺省为左对齐，可取的值 '<', '>', '^', None
    填充字符缺省为空格
    """
    width = width_east_str(text)
    if width >= min_width: return text
    fill_width = min_width - width
    if justify == '>' :  # right justified
        return fill_width * fillchar + text
    elif justify == None or justify == '<':
        return  text + fill_width * fillchar
    else:  # center
        return (fill_width+1) // 2 * fillchar + text  + fill_width // 2 * fillchar


def test_format_east_str():
    text1 = '中国12上海'
    text2 = 'Shanghai'
    print('(%s)' % format_east_str(text1, 20))
    print('(%s)' % format_east_str(text2, 20))

    print('(%s) (%s) (%s)' % (format_east_str(text1, 20, '>', ' '), format_east_str(text1, 20, '<', ' '), format_east_str(text1, 20, '^', '*')))
    print('(%s) (%s) (%s)' % (format_east_str(text2, 20, '>', ' '), format_east_str(text2, 20, '<', ' '), format_east_str(text2, 20, '^', '*')))
    print('(%s) (%s) (%s)' % (format_east_str(text1, 20, '>', ' '), format_east_str(text2, 20, '<', ' '), format_east_str(text1, 20, '^', '*')))


class ChineseStringFormatter(Formatter):
    """ 中英文混合的字符串的格式化支持
    当要格式化的对象为str并且格式化描述符为C时使用
    格式化C支持下面格式：
    [[fill]align][minimumwidth][.precision][type]

    """
    def __init__(self):
        Formatter.__init__(self)

    def format_chinese_str(value, format_spec):
        """ [[fill]align][minimumwidth][.precision][type]
        align in (^, < , > or None (default=<)
        """
        fill = ' '
        align = '<'

        consumed = 0
        if format_spec == 'C':
            return value
        # first remove last type code C, and parse precision
        first, sep, last = format_spec[:-1].rpartition('.')
        if not sep:
            first = last
        else:
            try:
               precision = int(last)
            except ValueError:
                raise ValueError(' Format specifier missing precision')
            value = value[:precision]
            if not first:
                return value

        # now first = [[fill]align][minimumwidth]
        if len(first) > 1 and first[1] in '^<>':
            align = first[1]
            fill = first[0]
            consumed = 2
        elif len(first) > 0 and first[0] in '^<>':
            align = first[0]
            consumed = 1   # 1 char should be removed
        elif len(first) > 0 and not first[0].isdigit():
            fill = first[0]
            consumed = 1
        width = first[consumed:]
        try:
            width = int(width)
        except ValueError:
            raise ValueError('Invalid format specifier')
        # print('fill=%s, align=%s, width=%s, value=%s' % (fill, align, width, value))
        return format_east_str(value, width, align, fill)


    def format_field(self, value, format_spec):
        if type(value) == str and format_spec[-1] == 'C':
            return ChineseStringFormatter.format_chinese_str(value, format_spec)
        else:
            return format(value, format_spec)

def test_formatter():
    fmt = ChineseStringFormatter()
    text1 = '中国12上海'
    text2 = 'Shanghai'
    print(fmt.format('({text:20C}) ({text:*^20C}) ({text:>20C})', text=text1))
    print(fmt.format('({text:20C}) ({text:*^20C}) ({text:>20C})', text=text2))

    print(fmt.format('{:d} {:^5s} {:5.2f}', 1234, 'fmt', 3.1415))

if __name__ == '__main__':
    test_format_east_str()
    print()
    test_formatter()
