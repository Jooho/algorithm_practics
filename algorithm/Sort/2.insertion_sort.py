#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
__author__ = "jooholee"
__maintainer__ = "jooholee"
__date__ = "2018/Feb/13"
__description__ = 삽입정렬
                  - 리스트의 값을 한개씩 추가하면서 정렬하는 방식
                  - 첫번째/두번째 => 정렬
                  - 첫번째/두번째/세번째 => 정렬
                  - 첫번째/두번째/세번째/네번째 ==> 정렬
__license__ = "GPL"
__version__ = "0.9"

__email__ = "ljhiyh@gmail.com"
__status__ = "Development"
__copyright__ = "Copyright 2018, The python_practice project"
"""
import random

import time

debug = False
test_data = []
data_size = 10000  # 10000부터 급격히 느려짐(28초) 1000(0.2초)
data_move = 0
while len(test_data) < data_size:
    data = random.randrange(0, data_size)
    if not (data in test_data):
        test_data.append(data)


def move(data, index):
    global data_move
    # 데이값이 1개일때는 비교할 필요없음
    if index == 0:
        return

    min_index = index  # 리스트중 target data 들어갈 index
    data_length = index  # 리스트의 길이
    target_data = data[index]  # target data의 value

    # 리스트의 끝부터 차례차례 앞으로 가며 Target data가 들어가야하는 index위치를 찾는다.
    for check_index in reversed(range(data_length)):
        if debug:
            print(
                "Target Data: %d Checking index:%d Checking index data:%d" % (
                target_data, check_index, data[check_index]),
                end="\n")
        if target_data < data[check_index]:
            if debug: print("Check index data 가 target data보다 크기 때문에 min_index를 %d로 변경합니다" % check_index)
            min_index = check_index
    if debug:
        print("최종 결정된 min_index는 %d입니다." % (min_index))
        print("min_index(%d)부터 index(%d)까지 1칸씩 데이터를 이동한다." % (min_index, index))

    if min_index != index:
        for i in reversed(range(min_index, index)):
            data[i + 1] = data[i]
            data_move += 1
        if debug: print("마지막으로 target data(%d)를 min_index(%d)에 삽입한다." % (target_data, min_index))
        data[min_index] = target_data
    if debug:
        print(data)
        print(" -" + '-' * index * 3 + "|")


def sort():
    for index in range(len(test_data)):
        move(test_data, index)


if __name__ == '__main__':
    print("Test Data ===>", test_data, end="\n\n")

    start_time = time.time()

    sort()

    last_time = time.time()
    print("\n")
    print(last_time - start_time)

    print("\n")
    print("Total move: %d" % data_move)
    print("Sorted Data ===>", test_data)
