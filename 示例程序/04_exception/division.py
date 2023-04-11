#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

try:
    x = eval(input('请输入被除数: '))
    y = eval(input('请输入除数: '))
    z = x / y
except ZeroDivisionError:
    print('除数不能为零')
except TypeError:
    print('被除数和除数应为数值类型')
except NameError:
    print('变量不存在')
except Exception as e:   # except 等价于 except BaseException
    print(type(e), e)
else:
    print(x, '/', y, '=', z)

def division():
    try:
        x = eval(input('请输入被除数: '))   # [1,2][2],  Ctrl-C
        y = eval(input('请输入除数: '))
        z = x / y
        print('A')
    except (ZeroDivisionError, TypeError, NameError) as e:
        print(type(e), e)
        print('您的输入有误')
    except Exception as e:   # except 等价于 except BaseException
        print(type(e), e)
    else:
        print(x, '/', y, '=', z)
    finally:
        print('D')
    print('B')


if __name__ == '__main__':
    try:
        division()
    except KeyboardInterrupt as e:
        print('...')
    
    print('C')
