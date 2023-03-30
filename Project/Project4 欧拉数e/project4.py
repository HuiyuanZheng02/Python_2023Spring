'''
2023-03-30
@HuiyuanZheng02
'''
# 定义主函数
def main():
    # 初始化阶乘倒数、计数器、和
    factorial_inverse = count = 1
    sum = 0
    # 当阶乘倒数大于10的-12次方时，继续循环
    while factorial_inverse > 1e-12:
        # 累加阶乘倒数
        sum += factorial_inverse
        # 计算下一个阶乘倒数
        factorial_inverse /= count
        # 更新计数器
        count += 1
    # 输出自然常数e的值
    print("e = ", sum)

if __name__ == '__main__':
    main()