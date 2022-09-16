# N = 10
# -*- coding: utf-8 -*-
import time
import functools


def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('{} times:{}s'.format(func.__name__, end - start))

    return inner


@time_it
def func_1(N):
    count = 0
    for i in range(2, N):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += i
            continue
    print(count)


@time_it
def func_2(N):
    count = 0
    for i in range(2, N):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1
        if k == 2:
            count += i
    print(count)


n = int(input())
# n = 10000
f1 = func_1(n)
f2 = func_2(n)
