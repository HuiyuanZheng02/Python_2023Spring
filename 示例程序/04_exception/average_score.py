
def average_score1():
    """用户输入若干个成绩，直到用户直接回车，不输入任何信息（空字符串）时为止，计算平均分 """
    total = n = 0
    text = input("请输入成绩[0, 100]: ")
    while text:
        score = float(text)
        if 0 <= score <= 100:
            total += score
            n += 1
        else:
            print('请输入[0, 100]之间的成绩:')
        text = input("请输入成绩[0, 100]: ")

    if n > 0:
        print('平均成绩 = %.2f' % (total / n))

def average_score2():
    """用户输入若干个成绩，直到用户直接回车，不输入任何信息（空字符串）时为止，计算平均分 """
    total = n = 0
    text = input("请输入成绩[0, 100]: ")
    while text:
        try:
            score = float(text)
            if 0 <= score <= 100:
                total += score
                n += 1
            else:
                print('请输入[0, 100]之间的成绩:')
        except ValueError as e:
            print('非法的浮点数', e)

        text = input("请输入成绩[0, 100]: ")

    if n > 0:
        print('平均成绩 = %.2f' % (total / n))


def shortest_phrase():
    phrase = input('type a phrase (Enter to quit)? ')
    shortest = phrase
    while phrase:
        if len(phrase) < len(shortest):
            shortest = phrase
        phrase = input('type a phrase (Enter to quit)? ')

    print('shortest phrase was:', shortest)


if __name__ == '__main__':
    average_score1()
    shortest_phrase()
