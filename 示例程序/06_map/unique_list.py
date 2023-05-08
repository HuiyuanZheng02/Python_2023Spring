
import random

# 产生100个[0,10000)之间的随机整数，保存在列表中

listRandom = [random.choice(range(10000)) for i in range(100)]
print('initial list:')
print(*listRandom, end='\n\n')

# 循环+选择结构
noRepeat0 = []
for i in listRandom :
    if i not in noRepeat0 :
         noRepeat0.append(i)
print(*noRepeat0, end='\n\n')

noRepeat = list(set(listRandom))
print(*noRepeat, end='\n\n')


newDict = dict.fromkeys(listRandom)
noRepeat2 = list(newDict)
print(*noRepeat2, end='\n\n')

import collections

newDict = collections.OrderedDict.fromkeys(listRandom)
noRepeat3 = list(newDict)
print(*noRepeat3, end='\n\n')


newList = sorted(noRepeat, key=listRandom.index)
print(*newList, end='\n\n')

# 如果原地排序，则
# noRepeat.sort(key=listRandom.index)
