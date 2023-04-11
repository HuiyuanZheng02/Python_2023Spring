import datetime

now = datetime.datetime.now()
print('现在时刻：%d-%02d-%02d %02d:%02d' % (now.year, now.month, now.day, now.hour, now.minute))
delta_now = now - datetime.datetime(year=now.year, month=1, day=1)
print('今天是今年的第%d天' % (delta_now.days + 1) )

if now.month == 12:
    next_month = now.replace(year=now.year + 1, month=1, day=1)
else:
    next_month = now.replace(month=now.month + 1, day=1)
print('还有%d天到下个月' % (next_month - now).days)

interval = float(input('请输入一个时间间隔（分钟）'))
future = now + datetime.timedelta(minutes=interval)
print(future.ctime())
print(future.strftime('%Y-%m-%d %H:%M:%S'))
print('过去了%d天' % (future.toordinal() - now.toordinal()))
print('那一天是', future.strftime('%A'))
