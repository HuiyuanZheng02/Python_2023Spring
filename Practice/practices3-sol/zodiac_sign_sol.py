"""
下面给出了星座与所对应的日期的对应表，要求根据用户输入的月份和日期，返回其所属的星座：
提示可以利用元组或列表对象的比较运算
Aquarius    水瓶座：1月21日～2月19日
Pisces      双鱼座：2月20日～3月20日
Aries       白羊座：3月21日～4月20日
Taurus      金牛座：4月21日～5月20日
Gemini      双子座：5月21日～6月21日
Cancer      巨蟹座：6月22日～7月23日
Leo         狮子座：7月24日～8月23日
Virgo       处女座：8月24日～9月23日
Libra       天秤座：9月24日～10月23日
Scorpio     天蝎座：10月24日～11月22日
Sagittarius 射手座：11月23日～12月21日
Capricorn   摩羯座：12月22日～1月20日
"""

ZODIAC_DAYS = ((1, 20), (2, 19), (3, 20), (4, 20), (5, 20),
               (6, 21), (7, 23), (8, 23), (9, 23), (10, 23),
               (11, 22), (12, 21))

ZODIAC_NAMES = ('魔蝎座', '水瓶座', '双鱼座', '白羊座', '金牛座',
                '双子座', '巨蟹座', '狮子座', '处女座', '天秤座',
                '天蝎座', '射手座')

# 可以利用元组的比较运算
def zodiac_sign(month, day):
    for i, item in enumerate(ZODIAC_DAYS):
        if (month, day) <= item:
            return ZODIAC_NAMES[i]
    return ZODIAC_NAMES[0]


if __name__ == '__main__':
    month, day = eval(input('please input month,day = '))
    print('%d月%d日是%s' % (month, day, zodiac_sign(month, day)))

