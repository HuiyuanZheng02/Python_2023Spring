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
    pass

def main():
    height = int(input('Please input height= '))
    assert height > 0, 'height should be positive integer!'
    draw_rocket_ship(height)

if __name__ == '__main__':
    main()
    