s = [10, 5, 23, 20]
s1 = sorted(s)
print(s1)

def weight(item):
    item = str(item)
    return int(item[::-1])

s2 = sorted(s, key=weight)
print(s2)

s3 = sorted(s, key=lambda item: int(str(item)[::-1]))
print(s3)

import random
random.seed(1234)
s = list(range(14))
random.shuffle(s)
print(s)
ss = s.copy()

def weight(item):
    return len(str(item))

s.sort(key=weight)
print(s)

ss.sort(key=lambda item: len(str(item)))
print(ss)

t  = [3, 4, 6, 7, 5, 9, 11, 17, 13, 15]
t.reverse()
print(t)

"""
>>> t.reverse()
>>> t
[15, 13, 17, 11, 9, 5, 7, 6, 4, 3]
"""

m = reversed(t)
print(type(m))
print(list(m))

for item in m:
    print(item)

print('-' * 40)

for item in reversed(t):
    print(item, end=', ')



cities = ['Shanghai', 'Beijing', 'Wuhan', 'Chengdu', 'Nanjing']
temperatures = [30, 26, 34, 29, 38] 
pairs = sorted(zip(temperatures, cities))
[item[1] for item in pairs] 
s_cities = [ x for _, x in sorted(zip(temperatures, cities))]
print(*s_cities)
