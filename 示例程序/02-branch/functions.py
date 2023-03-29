# import math

def distance(x, y):
    x = x * x   #1
    y = y * y
    x += y      #2
    return x ** 0.5
#    return math.sqrt(x) 

x = y = 6
z = distance(x, y+2)
print(z)



def f1():
    print('f1')

def f1(): print('f1')

def f2():
    pass

def cubic(x):
    return x ** 3

def abs2(x, y):
    z = x + y
    if z >= 0:
        return z
    else:
        return -z
   
def abs2(x: int, y: int) -> int:
    z = x + y
    if z >= 0:
        return z
    else:
        return -z

# 函数调用
f1()
c = cubic(4)
a = abs2(c, -4*6)
print(c, a)


def max_(x, y):
    if x > y:
        return x
    else:
        return y
def max2_(x, y):
    if x > y:
        print(x)
    else:
        print(y)

print(max_(2,4))
print(max2_(2, 4))


n = 3
result = cubic(n)
result = cubic(cubic(n))
result = cubic(cubic(cubic(n)))
