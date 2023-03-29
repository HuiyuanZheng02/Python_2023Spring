def draw_triangle1():
    for line in range(1, 6):
        print('#' * line)


def draw_triangle2():
    for line in range(1, 6):
        print('#' * line, end='')
        print('++' * line, end='')
        print('#' * line)

def draw_triangle3():
    for line in range(1, 6):
        print(" " * (line - 1), end="")
        print("*" * (11 - 2 * line))

def draw_triangle4():
    for line in range(1, 6):
        print(("*" * (11 - 2 * line)).center(9))

if __name__ == '__main__':
    draw_triangle1()
    print()
    draw_triangle2()
    print()
    draw_triangle3()
    print()
    draw_triangle4()
