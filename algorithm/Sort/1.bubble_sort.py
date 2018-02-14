#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
__author__ = "jooholee"
__maintainer__ = "jooholee"
__date__ = "2018/Feb/11"
__description__ = Bubble Sort가 정렬하는 방법
                - 리스트 값중 맨 나중에 있는 2개를 비교한다.
                - 둘 중 작은 값을 앞으로 SWAP한다.
                - 이 방식으로 맨 앞의 값까지 정리한다.
                - 처음부터 끝까지 N번 돌면 정렬이 끝난다.
                즉 최악의 시간 복잡도는 O(n^2)이 된다.

__license__ = "GPL"
__version__ = "0.9"

__email__ = "ljhiyh@gmail.com"
__status__ = "Development"
__copyright__ = "Copyright 2018, The python_practice project"
"""
import random

import time

data_size = 10000   # 10000부터 급격히 느려짐(40초)  1000(0.4초)
test_data = []
while len(test_data) < data_size:
    data = random.randrange(0, data_size)
    if not (data in test_data):
        test_data.append(data)
show_data = test_data[0:]
sorted = 0
total_swap = 0


def compare():
    global sorted
    global total_swap
    test_length = data_size
    while test_length > 1:
        test_length -= 1
        if test_data[test_length - 1] <= test_data[test_length]:
            pass
        else:
            total_swap += 1
            sorted += 1
            test_data[test_length - 1], test_data[test_length] = test_data[test_length], test_data[test_length - 1]

            # 위의 SWAP하는 방법을 풀면 아래와 같음
            # temp = test_data[test_length - 1]
            # test_data[test_length - 1] = test_data[test_length]
            # test_data[test_length] = temp
            # print(test_data)

if __name__ == '__main__':
    print(test_data)
    start_time = time.time()

    for i in range(data_size):
        if sorted != data_size:
            compare()
        else:
            break

    last_time = time.time()
    print("\n")
    print(last_time - start_time)

    print("\n")
    print("Sort Completion!!")
    print("Total Swap:%d!!" % (total_swap))
    print("unsorted_data = " + ','.join(map(str, show_data)))
    print("Sorted data =" + ','.join(map(str, test_data)))
