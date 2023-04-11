#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import sys
import traceback

def A():
    1/0

def B():
    A()

def C():
    B()


def traceback_demo():
    try:
        C()
    except:
        traceback.print_exc()

if __name__ == '__main__':
    try:
        4 / 0
    except:
        ex_type, ex_info, ex_traceback = sys.exc_info()
        print(ex_type, ex_info, ex_traceback)
        print('-----traceback object information-----')
        traceback.print_tb(ex_traceback)

        print('-----traceback.print_exception-----')
        traceback.print_exception(ex_type, ex_info, ex_traceback)

        print('-----traceback.print_exc-----')
        traceback.print_exc()

        #    print(''.join(traceback.format_tb(ex_traceback)))


       