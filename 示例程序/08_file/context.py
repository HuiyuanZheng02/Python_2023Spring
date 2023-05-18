#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import time


class Timer(object):
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()
        print('执行开始时刻：', time.strftime('%H:%M:%S', time.localtime(self.start)))

    def __exit__(self, exception_type, exception_val, trace):
        stop = time.time()
        print('执行结束时刻：', time.strftime('%H:%M:%S', time.localtime(stop)))
        print("耗时:%.4f" % (stop - self.start))



import contextlib
import time

@contextlib.contextmanager
def time_print(task_name):
    t = time.time()
    try:
        yield
    finally:
        print('%s took %.4f seconds' % (task_name, time.time() - t))

if __name__ == '__main__':
    with Timer():
        for i in range(10000000):
            pass

    with time_print("processes"):
        for i in range(10000000):
            pass
