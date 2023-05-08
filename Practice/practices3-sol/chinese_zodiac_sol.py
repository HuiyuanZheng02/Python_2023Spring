"""
编写一个函数get_chinese_zodiac(year)，其参数year为年份，将其转换为中国的生肖年份，
目前已知2000年是龙年

"""

CHINESE_ZODIACS='鼠牛虎兔龙蛇马羊猴鸡狗猪'
# 已知2000年是龙年


RAT_YEAR = 2000 - CHINESE_ZODIACS.index('龙')
def get_chinese_zodiac(year):
    zodiac = (year - RAT_YEAR) % 12
    return CHINESE_ZODIACS[zodiac]

if name == '__main__':
    year = int(input('please input year = '))
    print('%d是%年' % (year, get_chinese_zodiac(year)))

