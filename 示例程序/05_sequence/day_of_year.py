#!/usr/bin/env python3

""" 今天是今年的第几天
    1. 首先得到今天对应的年份、月份和当月第几天
    2. 今年的第几天=前面的月份天数之和+当月第几天

2月的天数随闰年而不同, 怎么判断闰年？
* 能被4整除，但不能被100整除
* 能被400整除
"""

def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def yday(date):
    """ date是今年的第几天?
    今年的第几天=前面的月份天数之和+当月第几天
    2月的天数随闰年而不同, 怎么判断闰年？
    * 能被4整除，但不能被100整除
    * 能被400整除

    @date: 传递一个序列，前面3个元素为year, month, day
    """

    day_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    year, month, day, *_ = date
    if month == 1:
        return day
    yday_ = sum(day_month[:month-1]) + day
    if month > 2 and is_leap_year(year):
        yday_ += 1
    return yday_

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

dbm = 0
DAYS_BEFORE_MONTH = [0]
for dim in DAYS_IN_MONTH[:-1]:
    dbm += dim
    DAYS_BEFORE_MONTH.append(dbm)
# print(DAYS_BEFORE_MONTH)
del dbm, dim

def yday2(date):
    """ date是今年的第几天
       1. 首先得到date对应的年份、月份和当月第几天
       2. 今年的第几天=前面的月份天数之和+当月第几天
    2月的天数随闰年而不同, 怎么判断闰年？
    * 能被4整除，但不能被100整除
    * 能被400整除

    @date: 传递一个序列，前面3个元素为year, month, day
    """

    year, month, day, *_ = date
    yday_ = DAYS_BEFORE_MONTH[month-1] + day
    if month > 2:
        if is_leap_year(year):
            yday_ += 1
    return yday_



def test_yday():
    import time
    date = time.localtime()
    print('%4d-%02d-%02d 是今年的第%d天' % (date[0], date[1], date[2], yday(date)))


if __name__ == '__main__':
    print('-'*40)
    test_yday()
