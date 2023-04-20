"""
求解n以内的素数
如果一个数可以分解成多个因子的成绩，则不是素数，进一步其可以分解成多个素因子的成绩
2是素数，2*2, 2*3, 2*4,...等不是素数
3是素数, 3*2, 3*3, 3*4, ...等不是素数
4不是素数，说明其有更小的素因子，不需要考虑
5是素数, 5*2, 5*3, ....等不是素数

所有可能的素因子factor in [2, sqrt(n)], factor * 2, factor * 3... 一定不是素数
"""
import math

def sieve(n):
    if not isinstance(n, int) or n < 2:
        raise ValueError('n必须为正整数')
    return [2]


if __name__ == '__main__':
    primes = sieve(100)
    print("小于等于n的素数有%d个：\n" % len(primes),*primes)
