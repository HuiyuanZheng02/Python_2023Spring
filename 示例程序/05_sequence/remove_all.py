#!/usr/bin/env python3

class my_list(list):
    ''' list迭代器的类似实现，供参考 '''
    def __iter__(self):
        class iterator():
            def __init__(self,obj):
                self.obj = obj
                self.pos = 0
#                print('init obj = %s' % self.obj)

            def __next__(self):
                if self.pos >= len(self.obj):
                    raise StopIteration()
                self.pos += 1
                print('pos=%d\tvalue=%s\tobj=%s' % (self.pos-1, self.obj[self.pos-1], self.obj))
                return self.obj[self.pos-1]

        return iterator(self)

"""
for item in iterable:
    print(item)
"""

def remove_all(list_, value):
    """ 教材上的例子，for循环中的可迭代对象在循环中被改变了时需要特别小心 """
    for item in list_:
        if item == value:
            list_.remove(value)
    return list_


def remove_all_0(list_, value):
    for i in range(len(list_)):
        print(i)
        if list_[i] == value:  # 会报错
            del list_[i]
    return list_


def remove_all_1(list_, value):
    for i in range(len(list_)):
        print(i)
        try:
            if list_[i] == value:  # 会报错
                del list_[i]
        except IndexError as e:
            print(e)
            import traceback
            traceback.print_exc()

            break
    return list_


def remove_all_2(list_, value):
    for item in list_[:]:
        if item == value:
            list_.remove(value)
    return list_


def remove_all_3(list_, value):
    for i in range(len(list_) - 1, -1, -1):
        if list_[i] == value:
            del list_[i]
    return list_


def remove_all_4(list_, value):
    i = 0
    while i < len(list_):
        if list_[i] == value:
            del list_[i] #不需要更新i
        else:
            i = i + 1
    return list_


def test_remove():
    x = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    x = my_list(x)
    print('remove_all(%s, %d)' %(x, 1))
    print(remove_all(x, 1))
    print('-' * 40)

    x = [1, 2, 1, 2, 1, 1, 1]
    x = my_list(x)
    print('remove_all(%s,%d)' %(x, 1))
    print(remove_all(x, 1))
    print('-' * 40)

    x = [1, 2, 1, 2, 1, 1, 1]
    print('remove_all_1(%s,%d):for i in range(len(list_))' %(x, 1))
    print(remove_all_1(x, 1))
    print('-' * 40)

    x = [1, 2, 1, 2, 1, 1, 1]
    print('remove_all_2(%s,%d):for item in list_[::]:' %(x, 1))

    print(remove_all_2(x, 1))
    print('-' * 40)

    x = [1, 2, 1, 2, 1, 1, 1]
    print('remove_all_3(%s,%d):for i in range(len(list_)-1,-1,-1): '  %(x, 1))
    print(remove_all_3(x, 1))
    print('-' * 40)

    x = [1, 2, 1, 2, 1, 1, 1]
    print('remove_all_4(%s,%d):while: '  %(x, 1))
    print(remove_all_4(x, 1))
    print('-' * 40)


if __name__ == '__main__':
    test_remove()
