"""模拟某个综艺节目观众给表演者评分：
从观众处得到一系列的打分，直到空字符为止。去掉一个最高分和最低分，按照分数顺序从低到高排列

请给表演者打分...95
请给表演者打分...80
请给表演者打分...75
请给表演者打分...98
请给表演者打分...88
请给表演者打分...77.0
请给表演者打分...67
请给表演者打分...
[75.0, 77.0, 80.0, 88.0, 95.0]

"""

def scores():
    all_scores = []
    while True:
        text = input('请给表演者打分...')
        if not text:
            break
        all_scores.append(float(text))
    all_scores.sort()
    return all_scores[1:-1]


def scores2():
    all_scores = []
    while True:
        text = input('请给表演者打分...')
        if not text:
            break
        try:
            all_scores.append(float(text))
        except Exception as e:
            print(type(e), e)

    all_scores.sort()
    return all_scores[1:-1]


if __name__ == '__main__':
    result = scores()
    print(result)
