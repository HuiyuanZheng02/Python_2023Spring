#!/usr/bin/env python3

def pyt_firstN_list(nums):
    ''' 毕达哥拉斯三元数组：存在{x,y,z}, 0<x<y<z,使得x^2+y^2=z^2 '''
    pyt = [(x,y,z) for z in range(1000) for y in range(1,z) for x in range(1,y) if x*x + y*y == z*z ]
    firstN_pyt = pyt[:nums]
    print(*firstN_pyt)


# N ** 3 
def pyt_firstN_loop(nums):
    ''' 毕达哥拉斯三元数组：存在{x,y,z}, 0<x<y<z,使得x^2+y^2=z^2 '''
    firstN_pyt = []
    z = 1
    while True:
        for y in range(1, z):
            for x in range(1, y):
                if x*x + y*y == z*z:
                    firstN_pyt.append((x,y,z))
                    if len(firstN_pyt) == nums:
                        break
            if len(firstN_pyt) == nums:
                break
        if len(firstN_pyt) == nums:
            break
        z += 1
    print(*firstN_pyt)


# tuple generator expression: generator version of list comprehension, also an iterator

def pyt_firstN_generator(nums):
	# pythogorian triplets (x,y,z), 0<x<y<z, x*x + y*y = z*z
    pyt = ((x,y,z) for z in range(10000) for y in range(1,z) for x in range(1,y) if x*x + y*y == z*z )
    firstN_pyt = [next(pyt) for x in range(nums) ]
    print(*firstN_pyt)


if __name__ == '__main__':
    pyt_firstN_list(10)
    print('-' * 40)
    pyt_firstN_loop(10)
    print('-' * 40)
    pyt_firstN_generator(10)
    print('-' * 40)
