'''
2023-06-06
@HuiyuanZheng02
'''
import random
import time
import csv
import os
from datetime import datetime

# 用户类
class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.points = 0

    # 增加积分
    def add_points(self, points):
        self.points += points

    # 减少积分
    def subtract_points(self, points):
        if self.points >= points:
            self.points -= points
            return True
        return False

# 抽奖类
class Lottery:
    def __init__(self):
        self.users = {}
        self.winners = []

    # 添加用户
    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    # 更新积分
    def update_points(self, user_id, points):
        if user_id in self.users:
            if points > 0:
                self.users[user_id].add_points(points)
            else:
                return self.users[user_id].subtract_points(abs(points))
        return True

    # 抽奖
    def draw_lottery(self):
        first_prize_candidates = []
        second_prize_candidates = []
        
        for user_id, user in self.users.items():
            if user.points >= 1000 and user_id not in self.winners:
                first_prize_candidates.append((user_id, user.points))
        first_prize_winner = self.draw_first_prize(first_prize_candidates)

        for user_id, user in self.users.items():
            if user.points > 0 and user_id not in self.winners and user_id != first_prize_winner:
                second_prize_candidates.append(user_id)
        second_prize_winners = self.draw_second_prize(second_prize_candidates, 2)

        return first_prize_winner, second_prize_winners

    # 抽一等奖
    def draw_first_prize(self, candidates):
        if not candidates:
            return None

        weighted_candidates = []
        for user_id, points in candidates:
            weight = 1
            if 1000 <= points < 2000:
                weight = 1
            elif 2000 <= points < 3000:
                weight = 2
            elif points >= 3000:
                weight = 3
            weighted_candidates.extend([user_id] * weight)

        return random.choice(weighted_candidates)

    # 抽二等奖
    def draw_second_prize(self, candidates, num_winners):
        if not candidates:
            return []
        return random.sample(candidates, min(num_winners, len(candidates)))

'''
程序不定时随机产生上述两种事件，其中的有效事件需要追加到 updates.csv 文件末尾 (若文件不存在则新建)。
文件每行为一次变动记录，包含:用户 ID 和积分变动数量 (正负整数)。
将该次积分变动显示在屏幕上。
'''
def simulation_credit_update(lottery):
    user_id = random.choice(list(lottery.users.keys()))  # 随机选择一个用户ID
    points = random.randint(-1000, 1000)  # 随机产生积分变动

    valid_update = lottery.update_points(user_id, points)
    if valid_update:
        if not os.path.exists("updates.csv"):  #  若文件不存在则新建
            with open("updates.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["User ID", "Points"])
        with open("updates.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([user_id, points])
        if points >= 0: print(f"{user_id}, +{points}")
        else: print(f"{user_id}, {points}")


# 主函数
def main(user_num, test=False, update_times=100):
    '''
    @param user_num: 用户数量
    @param test: 用于测试,缺省为False. True时开启测试模式,积分更新次数由update_times指定,更新结束后开始抽奖, 每隔10秒一轮
    @param update_times: 测试模式下的模拟积分更新次数(包含失败情况)
    '''
    # 初始化用户，默认开始时用户积分为 0
    lottery = Lottery()
    for i in range(user_num):
        user = User(i)
        lottery.add_user(i)

    updated_times = 0

    print("积分变动: ")
    # 模拟积分更新
    while True:
        if test:
            if updated_times >= update_times:
                break
        else:
            if datetime.now().weekday() == 5 and datetime.now().hour == 22 and datetime.now().minute >= 57:
                break # 抽奖前3分钟停止积分更新
        if not test: time.sleep(random.randint(1, 10))  # 随机等待时间
        simulation_credit_update(lottery)
        updated_times += 1

    while True:
        '''
        每周第一轮抽奖开始时，将所有用户的当前积分信息写入 Candidates.csv 文件中(若文件已存在，清空原有内容)。
        每行为一个人的信息，包含:用户 ID 和当前积分，以逗号分隔。
        用户ID和积分都是大于等于 0 的整数。
        将所有用户的当前积分显示在屏幕上。
        '''
        # 每周六晚上23:00至23:40进行抽奖，共3轮，每轮间隔20分钟
        if datetime.now().weekday() == 5 and datetime.now().hour == 23 or test:
            with open("Candidates.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["User ID", "Points"])
                print("当前用户积分:")
                for user_id, user in lottery.users.items():
                    writer.writerow([user_id, user.points])
                    print(f"{user_id} : {user.points}")

            for round_num in range(1, 4):
                if round_num == 1: print("抽奖开始:")
                print(f"第{round_num}轮:")
                first_prize_winner, second_prize_winners = lottery.draw_lottery()

                if first_prize_winner is not None:
                    print(f"{first_prize_winner} 一等奖")
                    lottery.winners.append(first_prize_winner)

                for winner in second_prize_winners:
                    print(f"{winner} 二等奖")
                    lottery.winners.append(winner)

                if len(lottery.winners) == len([user_id for user_id in lottery.users if lottery.users[user_id].points > 0]) or round_num == 3:
                    print("本周抽奖结束")
                    break

                # 下一轮抽奖前等待20分钟
                if test: time.sleep(10) #test
                else: time.sleep(20 * 60)

            break
            
    # 归档updates.csv
    today = datetime.now().strftime("%Y-%m-%d")
    os.rename("updates.csv", f"{today}.csv")

if __name__ == "__main__":
    main(user_num=1000)
    # main(100, test=True, update_times=100)

