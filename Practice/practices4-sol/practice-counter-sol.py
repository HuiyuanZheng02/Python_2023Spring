"""
课堂上介绍了collections.Counter对象，该对象有两个方法elements()和most_common()
我们这里要求实现3个类似的函数，分别是get_elements(d)、iter_elements(d)和most_common(d)
"""

def get_elements(d):
    """ 
    实现 get_elements(d)
    d: {'a':3, 'b':2, 'c':1}
    输出 ['a', 'a', 'a', 'b', 'b', 'c']
    """
    e = []
    for key, count in d.items():
        for i in range(count):
            e.append(key)
        # or e.update([key] * count)
    return e

def iter_elements(d):
    """ 
    实现 iter_elements(d)
    d: {'a':3, 'b':2, 'c':1}
    输出一个迭代器对象，每个元素分别是'a', 'a', 'a', 'b', 'b', 'c'
    提示：可采用生成器函数实现
    """
    for key, count in d.items():
        for i in range(count):
            yield key

def most_common(d, n):
    """ 
    实现most_common(d, n)
    >>> d = {'b': 4, 'a': 5, 'd': 2, 'c': 3,  'e': 1}
    >>> most_common(d, 3)
    [('a', 5), ('b', 4), ('c', 3)]
    """
    m = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return m[:n]

if __name__ == '__main__':
    d = {'b': 4, 'a': 5, 'd': 2, 'c': 3,  'e': 1}
    elements = get_elements(d)
    print(elements)

    print(list(iter_elements(d)))

    m = most_common(d, 3)
    print(m)