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

test_length = 10
test_data = [random.randrange(0, test_length) for i in range(test_length)]
show_data = test_data[0:]
sorted = 0
total_swap = 0


def compare():
    global sorted
    global total_swap
    test_length = len(test_data)
    while test_length > 1:
        test_length -= 1
        if test_data[test_length - 1] <= test_data[test_length]:
            pass
        else:
            total_swap += 1
            sorted += 1
            temp = test_data[test_length - 1]
            test_data[test_length - 1] = test_data[test_length]
            test_data[test_length] = temp


if __name__ == '__main__':
    for i in range(test_length):
        if sorted != test_length:
            compare()
        else:
            break
    print("Sort Completion!!")
    print("Total Swap:%d!!" % (total_swap))
    print("unsorted_data = " + ','.join(map(str, show_data)))
    print("Sorted data =" + ','.join(map(str, test_data)))
