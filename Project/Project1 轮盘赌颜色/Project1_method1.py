
# Project 1 轮盘赌颜色
pocket = eval(input('请输入轮盘赌的pocket编号(0-36)==>'))
if pocket == 0:
    print("编号",pocket,"的pocket颜色为绿色",sep="")
################ 方法一：################
elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
    if pocket % 2:
        print("编号",pocket,"的pocket颜色为红色",sep="")
    else:
        print("编号",pocket,"的pocket颜色为黑色",sep="")
elif 11 <= pocket <= 18 or 29 <= pocket <= 36:
    if pocket % 2:
        print("编号",pocket,"的pocket颜色为黑色",sep="")
    else:
        print("编号",pocket,"的pocket颜色为红色",sep="")
else:
    print("编号不在[0,36]")