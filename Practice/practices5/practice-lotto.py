"""
模仿彩票游戏
首先用户随机生成一组彩票号码，接下来进行抽奖，给出彩票中奖的结果

你的彩票: 6 9 10 17 26 36
开奖号码: 4 7 14 16 31 34
很遗憾，您没有中奖

你的彩票: 1 9 23 25 28 31
开奖号码: 1 5 15 19 24 28
中奖数字: 1 28

"""

import random

def generate_random_ticket(n=6, max_num=36):
    """
    param: n 多少个数字
    param: max_num，数字的范围[1, max_num]
    """
    ticket = set()
    while len(ticket) < n:
        num = random.randint(1, max_num)
        ticket.add(num)
    return ticket

def winning_result(ticket, lottery):
    """
    param: ticket 彩票
    param: lottery 开奖数字
    输出兑奖结果
    """
    matches = ticket.intersection(lottery)
    print('你的彩票:', *sorted(ticket))
    print('开奖号码:', *sorted(lottery))
    if len(matches):
        print('中奖数字:', *sorted(matches))
    else:
        print('很遗憾，您没有中奖')

if __name__ == '__main__':
    ticket = generate_random_ticket()
    lottery = generate_random_ticket()
    winning_result(ticket, lottery)

    
