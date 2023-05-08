"""输出火箭船的ASCII艺术图，下面是参数height=3时的输出
     /**\
    //**\\
   ///**\\\
  ////**\\\\
 /////**\\\\\
+=*=*=*=*=*=*+
|../\..../\..|
|./\/\../\/\.|
|/\/\/\/\/\/\|
|\/\/\/\/\/\/|
|.\/\/..\/\/.|
|..\/....\/..|
+=*=*=*=*=*=*+
|\/\/\/\/\/\/|
|.\/\/..\/\/.|
|..\/....\/..|
|../\..../\..|
|./\/\../\/\.|
|/\/\/\/\/\/\|
+=*=*=*=*=*=*+
     /**\
    //**\\
   ///**\\\
  ////**\\\\
 /////**\\\\\

下面是参数height=4的输出：

       /**\
      //**\\
     ///**\\\
    ////**\\\\
   /////**\\\\\
  //////**\\\\\\
 ///////**\\\\\\\
+=*=*=*=*=*=*=*=*+
|.../\....../\...|
|../\/\..../\/\..|
|./\/\/\../\/\/\.|
|/\/\/\/\/\/\/\/\|
|\/\/\/\/\/\/\/\/|
|.\/\/\/..\/\/\/.|
|..\/\/....\/\/..|
|...\/......\/...|
+=*=*=*=*=*=*=*=*+
|\/\/\/\/\/\/\/\/|
|.\/\/\/..\/\/\/.|
|..\/\/....\/\/..|
|...\/......\/...|
|.../\....../\...|
|../\/\..../\/\..|
|./\/\/\../\/\/\.|
|/\/\/\/\/\/\/\/\|
+=*=*=*=*=*=*=*=*+
       /**\
      //**\\
     ///**\\\
    ////**\\\\
   /////**\\\\\
  //////**\\\\\\
 ///////**\\\\\\\
"""

def draw_rocket_ship(height):
    drawCone(height)
    drawLine(height)
    drawHalf1(height)
    drawHalf2(height)
    drawLine(height)
    drawHalf2(height)
    drawHalf1(height)
    drawLine(height)
    drawCone(height)

# Draws a cone that appears as both the nosecone and exhaust of the
# rocket ship.
def drawCone(height):
    for line in range(1, 2 * height, 1):
        for count in range(1, 2 * height - line + 1, 1):
            print(" ", end='')
        for count in range(1, line + 1, 1):
            print("/", end='')
        print("**", end='')
        for count in range(1, line + 1, 1):
            print("\\", end='')
        print()


# Draws a solid line
def drawLine(height):
    print("+", end='')
    for count in range(1, 2 * height + 1, 1):
        print("=*", end='')
    print("+")


# Draws one half of the subfigures, the part that point upwards.
def drawHalf1(height):
    for line in range(1, height + 1, 1):
        print("|", end='')
        for count in range(1, height - line + 1, 1):
            print(".", end='')
        for count in range( 1, line + 1, 1):
            print("/\\", end='')
        for count in range(1, 2 * height - 2 * line + 1, 1):
            print(".", end='')
        for count in range(1, line + 1, 1):
            print("/\\", end='')
        for count in range(1, height - line + 1, 1):
            print(".", end='')
        print("|")


# Draws one half of the subfigures, the part that point downwards.
def drawHalf2(height):
    for line in range(height, 0, -1):
        print("|", end='')
        for count in range(1, height - line + 1, 1):
            print(".", end='')
        for count in range(1, line + 1, 1):
            print("\\/", end='')
        for count in range(1, 2 * height - 2 * line + 1, 1):
            print(".", end='')
        for count in range(1, line + 1, 1):
            print("\\/", end='')
        for count in range(1, height - line + 1, 1):
            print(".", end='')
        print("|")


def main():
    height = int(input('Please input height= '))
    assert height > 0, 'height should be positive integer!'
    draw_rocket_ship(height)

if __name__ == '__main__':
    main()
