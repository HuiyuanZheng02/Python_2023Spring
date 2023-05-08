"""
写程序,输出以下内容

1   1

1   2
2   2

1   3
2   3
3   3

1   4
2   4
3   4
4   4

"""

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, i, sep='\t')
    print()


