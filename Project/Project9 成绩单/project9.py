'''
2023-05-11
20302010071 - 郑惠元
'''
import project9_util as util

def calculate_average(score_sheet):
    """
    @description: 计算成绩单的平均分
    @param score_sheet: 待计算的成绩单
    @return: 平均分
    """
    total_score = 0
    for i in score_sheet:
        total_score += score_sheet[i][1]
    average_score = total_score / len(score_sheet)
    return average_score

def calculate_median(score_sheet):
    """ 
    @description: 计算成绩单的中位数
    @param score_sheet: 待计算的成绩单
    @return: 中位数
    """
    score_list = []
    for i in score_sheet:
        score_list.append(score_sheet[i][1])
    score_list.sort()
    length = len(score_list)
    if length % 2 == 0:
        median = (score_list[length//2-1] + score_list[length//2]) / 2
    else:
        median = score_list[length//2]
    return median

def print_score_sheet(score_sheet):
    """
    @description: 按照学生ID(整数类型)的顺序输出成绩单
    @param: score_sheet: 待打印的成绩单
    """
    print(f"{'ID':<6}{'Name':<15}{'Score':<5}")
    print("-"*25)
    idList = sorted(list(score_sheet))
    for i in idList:
        ID = i
        Name = score_sheet[i][0]
        Score = score_sheet[i][1]
        print(f"{ID:<6}{Name:<15}{Score:<5}")
    pass


def print_score_sheet_sorted(score_sheet):
    """
    @description: 按照成绩排序输出成绩单
    @param: score_sheet: 待打印的成绩单
    """
    print(f"{'ID':<6}{'Name':<15}{'Score':<5}")
    print("-"*25)
    sList = []
    for i in score_sheet:
        a = i
        b = score_sheet[i][0]
        c = score_sheet[i][1]
        sList.append((c,a,b))
    sList.sort()
    for j in sList:
        ID = j[1]
        Name = j[2]
        Score = j[0]
        print(f"{ID:<6}{Name:<15}{Score:<5}")
    pass

def print_score_count(score_sheet):
    """
    @description: 前 5 个出现次数最多的分数及其出现次数
    @param: score_sheet: 待打印的成绩单
    """
    score_dict = {}
    for i in score_sheet:
        score = score_sheet[i][1]
        if score in score_dict:
            score_dict[score].append(i)
        else:
            score_dict[score] = [i]
    sorted_score_dict = sorted(score_dict.items(), key=lambda x: (-len(x[1]), -x[0]))
    print(f"{'score':<8}{'Count':<5}")
    print("-"*16)
    for i in range(5):
        if i >= len(sorted_score_dict):
            break
        score, ids = sorted_score_dict[i]
        print(f"{score:<10}{len(ids):<5}")
    pass

def main():
    """
    @description: 主函数
    默认班级人数为10人
    """
    score_sheet = util.get_score_sheet(10)

    print(f"\n平均分：{calculate_average(score_sheet):.2f}, 中位数：{calculate_median(score_sheet):.2f}")
    print('\n按照学生ID(整数类型)的顺序输出成绩单如下:')
    print_score_sheet(score_sheet)

    print('\n\n按照成绩排序输出成绩单如下:')
    print_score_sheet_sorted(score_sheet)
    
    print("\n\n前 5 个出现次数最多的分数及其出现次数:")
    print_score_count(score_sheet)

if __name__ == '__main__':
    main()
