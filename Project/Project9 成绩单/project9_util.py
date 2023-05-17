#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import string

def get_name(min_chars=3, max_chars=8):
    """ 返回一个名字，长度介于min_chars和max_chars之间
    """
    VALID_CHARS = string.ascii_lowercase

    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)


def get_score():
    """ 返回一个分数，介于50和100之间
    """
    return random.randint(50,100)

ids_in_use = []

def get_id():
    """ 返回一个唯一的ID，在[1,999]之间
    """
    global ids_in_use    # 这一行可不要

    while True:
        s_id = random.randint(1, 999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id

def get_score_sheet(total=90):
    """ 获得某个班级的学生成绩单，学生总人数缺省为90人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化score_sheet
    score_sheet = dict()
    for _ in range(total):
        # score_sheet:  { s_id: [name,score]}
        s_id = get_id()
        score_sheet[s_id] = [get_name(), get_score()]
    return score_sheet

if __name__ == '__main__':
    score_sheet = get_score_sheet(70)
    print(score_sheet)
