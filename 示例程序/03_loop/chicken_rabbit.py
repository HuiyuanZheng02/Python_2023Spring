#!/usr/bin/env python3


def chicken_rabbit_cage(heads=30, feet=90):
    # 鸡兔同笼问题。假设共有鸡、兔30只，脚90只
    found = False
    for chickens in range(0, heads + 1):
        for rabbits in range(heads + 1):
            if (chickens + rabbits) == heads and (2 * chickens + 4 * rabbits) == feet:
                print('鸡%d只,兔%d只' % (chickens, rabbits))
                found = True
                break
        if found:
            break
 
    if not found:
        print('无解')


def chicken_rabbit_cage2(heads=30, feet=90):
    # 鸡兔同笼问题。假设共有鸡、兔30只，脚90只
    for chickens in range(0, heads + 1):
        if 2 * chickens + 4 * (heads - chickens) == feet:
            print('鸡%d只,兔%d只' % (chickens, heads - chickens))
            break
    else:
        print('无解')


def chicken_rabbit_cage3(heads=30, feet=90):
    result = [i for i in range(heads + 1) if 2 * i + (heads - i) * 4 == feet]
    if (result == ''):
        print('无解')
    else:
        print('鸡%d只,兔%d只' % (result[0], heads - result[0]))


if __name__ == '__main__':
    chicken_rabbit_cage()

    print('-' * 40)
    chicken_rabbit_cage2()

    print('-' * 40)
    chicken_rabbit_cage3()
