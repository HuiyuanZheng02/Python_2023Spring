import random

def is_sorted(seq):
    """ 判断seq是否已经按照从小到大的顺序排序好，即为单调递增序列
    """
    return False

def selection_sort(seq):
    """选择排序
    首先选择最小的放在第1个，然后选择第2小的放在第2个...
    比如 seq = [4, 5, 3, 2, 1]
    首先选择1放在第1个位置，seq --> [1, 5, 3, 2, 4]
    接下来从剩下的元素中选择一个最小的（即原始的序列中第2小的）放在第2个位置， seq --> [1, 2, 3, 5, 4] 
    下一轮选择3放在第3个位置, seq --> [1, 2, 3, 5, 4]
    下一轮选择4放在第4个位置，排序结束, seq --> [1, 2, 3, 4, 5]
    """

if __name__ == '__main__':
    seq = list(random.choices(range(30, 101), k=15))
    random.shuffle(seq)
    print(seq)
    selection_sort(seq)
    if is_sorted(seq):
        print(seq, '已经排序好')
    else:
        print(seq, '乱序')