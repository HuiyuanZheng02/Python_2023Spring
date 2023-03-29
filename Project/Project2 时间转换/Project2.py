'''
2023-03-16
20302010071 郑惠元
'''
def shift_time():
    time = int(input('请输入时间间隔(分钟):'))
    if time <= 0:
        print("输入的时间必须为正整数！")
        return
    day = time // (60 * 24)
    hour = (time % (60 * 24)) // 60
    min = time % 60
    if day > 0: print(f"{day}天", end="")
    if hour > 0: print(f"{hour}小时", end="")
    if min > 0: print(f"{min}分钟", end="")
    print("",sep="")
        
shift_time()