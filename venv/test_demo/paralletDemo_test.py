#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @project : API_Service
# @File    : test_1.py
# @Date    : 2021/6/15 3:07 下午
# @Author  : 李文良


# demo：
import pytest
import time
import threading


def test_01(aaa):
    print('测试用例1操作')
    time.sleep(5)


def test_02():
    print('测试用例2操作')


def run_case():

    start_time1 = time.time()
    t1=threading.Thread(target=test_01)
    t2 = threading.Thread(target=test_02)
    t1.start()
    t2.start()
    end_time1 = time.time()
    print(end_time1 - start_time1)



    start_time2 = time.time()
    test_01()
    test_02()

    end_time2 = time.time()
    print(end_time2 - start_time2)


if __name__ == "__main__":

        run_case()



#--workers=1 进程数量 相当于几台电脑
#--tests-per-worker=4 线程，相当于多少场景