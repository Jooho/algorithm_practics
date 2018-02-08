#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
__author__ = "jooholee"
__maintainer__ = "jooholee"
__date__ = "2018/Feb/07"
__description__ = 미로 찾기와 비슷한 알고리즘
                  미로 찾기는 동서남북을 찾는 것이라면 이 알고리즘은 한 포인트를 기준을 기준으로 8곳(북 북동 동 동남 남 남서 서 서북)을 모두 찾는다.
__license__ = "GPL"
__version__ = "0.9"

__email__ = "ljhiyh@gmail.com"
__status__ = "Development"
__copyright__ = "Copyright 2018, The python_practice project"
"""

test_cells = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0]
]
# Recursion count
recursion_count = 0

# Maze Map Size
height = len(test_cells)
width = len(test_cells[0])

# Maze Map Term
background_color = 0
image_color = 1
already_counted = 2


def count_cell(x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return 0
    elif test_cells[x][y] != image_color or test_cells[x][y] == already_counted:
        return 0
    else:
        test_cells[x][y] = already_counted
        print("now, we count (%d,%d)" % (x, y))
        return 1 + count_cell(x, y - 1) + count_cell(x + 1, y - 1) + count_cell(x + 1, y) + \
               count_cell(x + 1, y + 1) + count_cell(x, y + 1) + count_cell(x - 1, y + 1) + \
               count_cell(x - 1, y) + count_cell(x - 1, y - 1)


if __name__ == '__main__':
    # print("image_color cell count is %d" % (count_cell(3, 4))) # total 12
    # print("image_color cell count is %d" % (count_cell(1, 1))) # total 2
    print("image_color cell count is %d" % (count_cell(1, 7))) # total 3
