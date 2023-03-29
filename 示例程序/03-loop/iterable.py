s = '12345'
for ch in s:
    print(ch)

print()
for ch in s:
    print(ch)

# 迭代器的访问
it = iter(s)
for item in it:
    print(item)
print('another loop')
for item in it:
    print(item)


# 问题：检查字符串中是否有十进制数字
found = False
for ch in s:
    if '0' <= ch <= '9':
        print('found digit!')
        found = True
        break

if not found:
    print('no digit!')

for ch in s:
    if '0' <= ch <= '9':
        print('found digit!')
        break
else:
    print('no digit!')


# 问题：检查字符串中是否有十进制数字(5除外）
for ch in s:
    if ch == '5':
        continue
    if '0' <= ch <= '9':
        print('found!')
        break
else:
    print('not found!')


for i in range(5):
    print(i)
print('range(5)')
print('-'*30)

for i in range(5, 0, -1):
    print(i)
print('range(5,0,-1)')
print('-'*30)

for i in range(1, 66, 13):
    print(i)
print('range(1, 66, 13)')
print('-'*30)

r = range(5)
for i in r:
    print(i)

print('another loop')
for i in r:
    print(i)
print('two loops for range(5) ')
print('-'*30)

r = reversed(range(5))
for i in r:
    print(i)

print('another loop')
for i in r:
    print(i)
print('two loops for reversed(range(5)) ')
print('-'*30)


s = list(range(0,20,2))
for item in s:
    print(item)

print()
for i in range(len(s)):
    print(i + 1, s[i])

print('倒计时开始...')
import time
for i in range(9, -1, -1):
    time.sleep(1)
    print('\r%d\a' % i, end='')
print('\rfire!')

def main():
    courses = 5
    students = 25
    class_size = students / courses
    # class_size = students // courses    
    for i in range(class_size):
        print(i)


if __name__ == '__main__':
    main()
