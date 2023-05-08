import random
s = [random.randint(0,100) for i in range(100)]
print(s)
if len(set(s)) == len(s):
    print('no duplicated scores')
else:
    print('duplicated scores!')
