def triple_value_list(list_, value):
    """将列表中相应的值替换为3个同样的值，要求原地修改列表
        比如triple_value_list([1,2,3,1,1], 1)，列表变为[1,1,1,2,3,1,1,1,1,1,1]
    """

    i = 0
    while i < len(list_):
        if list_[i] == value:
            list_[i:i] = [value, value]
            i += 3
        else:
            i += 1
    return list_


if __name__ == '__main__':
    x = [1, 2, 1, 2, 1, 1, 1]
    triple_value_list(x, 1)
    print(x)
