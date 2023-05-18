import random
random.seed(1234567)
# 随机小写英文字母
r = random.randint(0, 25)
r = random.randrange(0, 26)
print("小写字母:", chr(r + ord('a')))

import string
print("小写字母:", random.choice(string.ascii_lowercase))


# [1, 100)之间随机选择4个不同的整数
print(random.sample(range(1, 100), 4))

s = list(range(20))
random.shuffle(s)
print(s)
