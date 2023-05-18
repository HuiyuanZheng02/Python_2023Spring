#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import random

"""
列表temperature_days纪录了某一年（共365天）的每一天的最高温度和最低温度  [0,40]
现在我们想要统计每天最高温度出现的次数，以及该温度出现在一年的哪些天。
提示： 采用字典, key=最高温度, value = [该温度出现的天数]，即
{0: [16, 32, 56], 1: [18, 118, 173, 264, 291], 2: [66, 69, 79, 89, 103].... }

Cels       Count	Days
-5             8	44 67 113 116 161 208 312 323
-4            11	65 84 88 93 128 241 290 299 321 327 330
-3             4	13 251 300 350


"""

def generate_temperature_days(total=365):
    t = []
    for _ in range(total):
        high = random.randint(-5, 41)
        low = random.randint(-5, high)
        t.append((high, low))
    return t

def days_by_high_temperature(temperature_days):
    d = {}
    # key = high, value [ day1, day2...]

    for day, (high, low) in enumerate(temperature_days, 1): 
       if high not in d:
           d[high] = [day]
           # d[high] = d.get(high, 0) + 1
       else:
           d[high].append(day)

        # # 2.
        # t = d.get(high, [])
        # t.append(day)
        # d[high] = t
        #
        # # 3.
        # d[high] = d.get(high, [])
        # d[high].append(day)
        #
        # # 4.
        # d.setdefault(high, []).append(day)

    # print(d)


    print('%-10s %5s\t%s' % ('Cels', 'Count', 'Days'))
    # key = high, value [ day1, day2...]

    for temp in sorted(d):
        print('%-10s %5s' % (temp, len(d[temp])), end='\t')
        print(*d[temp],sep=',')



if __name__ == '__main__':
    temperature_days = generate_temperature_days()
    print(temperature_days)
    days_by_high_temperature(temperature_days)
