#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
根据身高和体重计算BMI，并输出结果
bmi = 体重除以身高的平方。bmi的值：
超过或等于29.9时，肥胖
低于18.5时，体重过轻
[18.5, 24.9)，体重正常
[24.9, 29.9), 体重偏重

"""

def get_bmi(weight, height):
    """
    返回元组，第一个元素为计算出来的bmi，第二个元素为对应的体重状况提示
    """
    bmi = weight / (height * height)
    if bmi < 18.5:
        text = '体重过轻'
    elif bmi >= 29.9:
        text = '肥胖'
    elif bmi < 24.9:
        text = '体重正常'
    else:  # [24.9, 29.9)
        text = '体重偏重'
    return bmi, text



if __name__ == '__main__':
    height = float(input("请输入您的身高(单位为米):"))
    weight = float(input("请输入您的体重(单位为千克):"))
    bmi, state = get_bmi(weight, height)
    print("您的BMI指数为%.2f,%s!" % (bmi, state))

