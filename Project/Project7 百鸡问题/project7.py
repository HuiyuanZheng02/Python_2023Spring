'''
2023-04-20
@HuiyuanZheng02
'''

def chick_calc( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    返回一个包含了所有解的列表，比如[(0, 25, 75), (4, 18, 78)]
    """
    solutions = []
    for x in range(0, 100 // 5 + 1):
        for y in range(0, 100 // 3 + 1):
            z = 100 - x - y
            if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
                solutions.append((x, y, z))
    return solutions

    
def chick_calc_comphrehension( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    返回一个包含了所有解的列表, 比如[(0, 25, 75), (4, 18, 78)]
    """
    return [(x, y, 100 - x - y) for x in range(0, 100 // 5 + 1) for y in range(0, 100 // 3 + 1) if (100 - x - y) % 3 == 0 and 5 * x + 3 * y + (100 - x - y) // 3 == 100]



def print_solutions(solutions):
    """ solutions里面保存了之前找到的所有解，按照指定格式输出这些解
    """
    print(f"总共有{len(solutions)}个解")
    for solution in solutions:
        print(f"解{solutions.index(solution)}:鸡翁 {solution[0]} 鸡母 {solution[1]} 鸡雏 {solution[2]}")

if __name__ == '__main__':
    solutions = chick_calc()
    print_solutions(solutions)
    
    print()

    solutions = chick_calc_comphrehension()
    print_solutions(solutions)
