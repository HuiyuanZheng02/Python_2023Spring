"""
求解n以内的素数
如果一个数可以分解成多个因子的乘积，则不是素数
2是素数，2*2, 2*3, 2*4,...等不是素数
3是素数, 3*2, 3*3, 3*4, ...等不是素数
4不是素数，说明其有更小的素因子，不需要考虑
5是素数, 5*2, 5*3, ....等不是素数

所有可能的素因子factor in [2, sqrt(n)], 其倍数factor * 2, factor * 3... 一定不是素数
"""
import math

def sieve(n):
    if not isinstance(n, int) or n < 2:
        raise ValueError('n必须为正整数')
    primes = [True] * (n-1)   # [2,n]
    max_factor = int(math.sqrt(n))
    for factor in range(2, max_factor + 1):
        if primes[factor-2]:
            for j in range(2, n // factor + 1):
                primes[factor * j - 2] = False
    primes = [idx+2 for idx, isprime in enumerate(primes) if isprime]
    return primes


if __name__ == '__main__':
    primes = sieve(100)
    print("小于等于n的素数有%d个：\n" % len(primes),*primes)
