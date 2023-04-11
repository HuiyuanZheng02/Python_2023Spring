'''
2023-03-23
@HuiyuanZheng02
'''

def output(j):
    for x in range(j):
        for y in range(x, j):
            print('-', end='') # 第i行数字左侧会有(j - i + 1)个“-”，其中x为行数-1。
        for y in range(1, (x+1)*2):
            print(y, end='')   # 第i行的数字为1至(i*2-1)
        for y in range(x, j):
            print('-', end='') # 同理，第i行数字右侧也有(j - i + 1)个“-”。
        print()
    if j == 5 : print()

def main():
    n = int(input('please input n = '))
    i = n // 5
    j = n % 5
    for x in range(i):
        output(5)
    output(j)

if __name__ == '__main__':
    main()