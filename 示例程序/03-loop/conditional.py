
# 用户输入一个[0, 10)范围内的整数，如果正确great，否则wrong
number = int(input('please input a number[0, 10)'))
if number >= 0:
    if number < 10:
        print('Great!')
    else:
        print('Wrong!')
else:
    print('Wrong!')

number = int(input('please input a number[0, 10)'))
if number >= 0 and number < 10: # 0 <= number < 10
    print('Great!')
else:
    print('Wrong!')


x = 40
if x > 10 and input('Print Value(y/n)?') == 'y':
    print(x)

if x != 0 and 100 / x > 2:
    print('Great')


name = input('Please enter your name: ') or '<unknown>' 


i = 36
if i % 17 != 2 or i % 13 != 10:
    print(i, "不满足：被17整除余2且被13整除余10")
else: 
    print(i, "被17整除余2且被13整除余10")


i = 36
if not (i % 17 == 2 and i % 13 == 10):
    print(i, "不满足：被17整除余2且被13整除余10")
else: 
    print(i, "被17整除余2且被13整除余10")



"""
怎么判断闰年？
* 能被4整除，但不能被100整除
* 能被400整除
"""
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



