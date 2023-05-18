import sys
import math

def f1(x, y):
    x1 = x * x
    z = x1 + y*y
    print('z =', z)
    print('times =', times)  # 全局变量

    
def f2(x, y):
    x1 = x * x
    z = x1 + y*y
    print('z =', z)
    
    # 访问同名的位于全局名字空间的变量
    print(sys.modules[__name__].z)
    print(globals()['z'])
    
    print('times =', times)  # 全局变量
    
   
def f3(x, y):
    x1 = x * x
    z = x1 + y*y
    print('z =', z)
   
    print('times =', times)
    times = times + 1  # UnboundLocalError: local variable 'times' referenced before assignment


def f4(x, y):
    x1 = x * x
    z = x1 + y*y
    print('z =', z)

    global times
    print('times =', times)  
    times = times + 1

def f5(x):
    x[0] += 1
    
x = y = z = 2    
times = 1
f1(x, y)
print('-' * 40)
f2(x, y)
print('-' * 40)
f3(x, y)
print('-' * 40)
f4(x, y)
print('-' * 40)
print('times =', times)  

t = [1, 2, 3, 4]
print(t)
f5(t)
print(t)
