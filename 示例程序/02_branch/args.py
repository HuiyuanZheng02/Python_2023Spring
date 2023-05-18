def f(a, b, c):
    print(a, b, c)
    
f(1, 2, 3)


def func(a, b, c, x='x', y='y'):
    print(a, b, c, x, y)

"""
# 下述函数定义会抛出异常：SyntaxError: non-default argument follows default argument
def f(a, x='x', y):
    print(a, x, y)
"""

# func(1, 2)  # 抛出异常：TypeError: func() missing 1 required positional argument: 'c'
func(1, 2, 3)            # 1 2 3 x y
func(1, 2, 3, 4)         # 1 2 3 4 y
func(1, 2, 3, 4, 5)      # 1 2 3 4 5
# func(1, 2, 3, 4, 5, 6)   # TypeError: func() takes from 3 to 5 positional arguments but 6 were given


func(1, 2, 3)                # 1 2 3 x y
func(1, 2, 3, y=5)           # 1 2 3 x 5
func(b=1, a=2, c=3, y=5)     # 2 1 3 x 5
func(1, c=3, b=2, x=5)       # 1 2 3 5 y
# func(1, b=2, x=5)          #　TypeError: func() missing 1 required positional argument: 'c'
