# This program draws an hourglass figure
# of characters and numbers using nested loops.
SUB_HEIGHT = 5

# Prints a solid line of dashes.
def draw_line(height=5):
    print("+", end="")
    print("-" * (2 * height), end="")
    print("+")

# Produces the top half of the hourglass figure.
def draw_top(height=5):
    for line in range(1, height + 1):
        print("|", end="")
        print(" " * (line - 1), end="")
        print("\\", end="")
        for i in range(1, 2 * height - 2 * line + 1):
            print(i, end="")
        print("/", end="")
        print(" " * (line - 1), end="")
        print("|")

# Produces the bottom half of the hourglass figure.
def draw_bottom(height=5):
    for line in range(1, height + 1):
        print("|", end="")
        print(" " * (height - line), end="")
        print("/", end="")
        for i in range(2 * line - 2, 0, -1):
            print(i, end="")
        print("\\", end="")
        print(" " * (height - line), end="")
        print("|")

def draw_top(height=5):
    for line in range(1, height + 1):
        print("|" +  " " * (line - 1) + "\\", end="")
        for i in range(1, 2 * height - 2 * line + 1):
            print(i, end="")
        print("/" +  " " * (line - 1) + "|")

# Produces the bottom half of the hourglass figure.
def draw_bottom(height=5):
    for line in range(1, height + 1):
        print("|" +  " " * (height - line) + "/", end="")
        for i in range(2 * line - 2, 0, -1):
            print(i, end="")
        print("\\" +  " " * (height - line) + "|")

def main():
    height = input('please input height(default 5) ')
    if height:
        height = int(height)
    else:
        height = 5

    draw_line(height)
    draw_top(height)
    draw_bottom(height)
    draw_line(height)

if __name__ == '__main__':
    main()
