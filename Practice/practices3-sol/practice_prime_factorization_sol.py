import math
def prime_factorize(n=100):
    """ 分解质因数，比如 100 = 2 * 2 * 5 * 5 """
    # 2, 3, 5, .... sqrt(n)
    # factor:   if n % factor == 0,
    #  100 ： factor  n = 50   n = 25   n = 1
    if not isinstance(n, int) or not n >= 2:
        raise Exception(n,'必须是大于1的正整数')
    orig = n  # 保存要分解的整数
    factors = []
    for factor in (2, *range(3, int(math.sqrt(n)+1), 2)):
        while n % factor == 0:
            n = n // factor
            factors.append(factor)
        if n == 1:
            break

    if n != 1:  # len(factors)
        factors.append(n)

    # map(str,factors)将因子列表中的每个元素从整数变为字符串
    print(orig, '=', ' * '.join(map(str, factors)))
    # ' * '.join([str(i) for i in factors])


def prime_factorize2(n=100):
    if not isinstance(n, int) or not n >= 2:
        raise Exception(n,'必须是大于1的正整数')
    orig = n  # 保存要分解的整数
    factors = []
    factor = 2
    while factor < n + 1:
        while n % factor == 0:
            n = n // factor
            factors.append(factor)
        if n == 1:
            break
        factor += 1

    # map(str,factors)将因子列表中的每个元素从整数变为字符串
    print(orig, '=', ' * '.join(map(str, factors)))


def possible_factor(n):
    import math
    yield 2
    k = 3
    while k <= math.sqrt(n):
        yield k
        k += 2


def prime_factorize3(n=100):
    if not isinstance(n, int) or not n >= 2:
        raise Exception(n,'必须是大于1的正整数')
    orig = n  # 保存要分解的整数
    factors = []
    for factor in possible_factor(n):
        while n % factor == 0:
            n = n // factor
            factors.append(factor)

    if n != 1:
        factors.append(n)

    # map(str,factors)将因子列表中的每个元素从整数变为字符串
    print(orig, '=', ' * '.join(map(str, factors)))

if __name__  == '__main__':
    for n in range(120, 150):
        prime_factorize(n)
