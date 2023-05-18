#!/usr/bin/env python3

"""查找一个最小正整数, 要求满足: 被3除余2, 被5除余3, 被7除余4"""

def smallest_n1():
    i = 1
    while True:
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 4:
            break
        i += 1
    print(i)


def smallest_n2():
    i = 1
    while not (i % 3 == 2 and i % 5 == 3 and i % 7 == 4):
    # while i % 3 != 2 or i % 5 != 3 or i % 7 != 4
        i += 1
    print(i)


def smallest_n3():
    i = 1
    done = False
    while not done:
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 4:
            done = True
        else:
            i += 1
    print(i)


def smallest_n4(limit=20000):
    """问题2. 要求满足: 被6除余2, 被7除余4, 被9除余5, 有解
    可能无法找到解，增加条件 i < limit, limit default 20000 """
    i = 1
    found = False
    while i < limit:
        if i % 6 == 2 and i % 7 == 4 and i % 9 == 5:
            print(i)
            found = True
            break
        i += 1

    if not found:
        print('没有解')


def smallest_n5(limit=20000):
    """问题2. 要求满足: 被6除余2, 被7除余4, 被9除余5, 有解
    可能无法找到解，增加条件 i < limit, limit default 20000 """
    i = 1
    while i < limit:
        if i % 6 == 2 and i % 7 == 4 and i % 9 == 5:
            print(i)
            break
        i += 1

    if i >= limit:
        print('没有解')


def smallest_n6(limit=20000):
    """问题2. 要求满足: 被6除余2, 被7除余4, 被9除余5, 有解
    可能无法找到解，增加条件 i < limit, limit default 20000 """
    i = 1
    found = False
    while not found and i < limit:
        if i % 6 == 2 and i % 7 == 4 and i % 9 == 5:
            print(i)
            found = True
        else:
            i += 1

    if not found:
        print('没有解')


def smallest_n7(limit=20000):
    """问题3. 要求满足: 被6除余2, 被7除余4, 被9除余4, 有解
    可能无法找到解，增加条件 i < limit, limit default 20000 """
    i = 1
    found = False
    while not found and i < limit:
        if i % 6 == 2 and i % 7 == 4 and i % 9 ==4:
            print(i)
            found = True
        else:
            i += 1

    if not found:
        print('没有解')

def smallest_n8(limit=20000):
    """问题2. 要求满足: 被6除余2, 被7除余4, 被9除余5, 有解
    可能无法找到解，增加条件 i < limit, limit default 20000 """
    i = 1
    while i < limit:
        if i % 6 == 2 and i % 7 == 4 and i % 9 == 5:
            print(i)
            break
        i += 1
    else:
        print('没有解')


if __name__ == '__main__':
    smallest_n1()
    smallest_n2()
    smallest_n3()
    smallest_n4()
    smallest_n5()
