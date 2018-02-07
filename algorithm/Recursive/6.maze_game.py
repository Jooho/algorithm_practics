#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
__author__ = "jooholee"
__maintainer__ = "jooholee"
__date__ = "2018/Feb/06"
__description__ = 미로 찾기 게임.
                  - 벽을 만났을때나 재방문을 했을때는 False값을 리턴
                  - 맨 마지막 위치에 도착하면 True리턴
                  - 동서남북을 돌아다니면서 길을 찾다가 결국 맨 마지막 위치에 못 도착하면 False를 리턴


__license__ = "GPL"
__version__ = "0.9"

__email__ = "ljhiyh@gmail.com"
__status__ = "Development"
__copyright__ = "Copyright 2018, The python_practice project"
"""
import os
import sys

sys.setrecursionlimit(100000)

test_maze = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0]
]

# Recursion count
recursion_count = 0

# Maze Map Size
height = len(test_maze)
width = len(test_maze[0])

# Maze Map Term
pathway = 0
wall = 1
visited = 2
wrong_path_way = 3
path = 4


def printPages():
    os.system("clear")
    for i in range(height):
        for j in range(width):
            if test_maze[i][j] == 0:
                print("=", end="")
            elif test_maze[i][j] == 1:
                print("*", end="")
            elif test_maze[i][j] == 2:
                print("-", end="")
            elif test_maze[i][j] == 3:
                print("X", end="")
            else:
                print("O", end="")

            if j == width - 1:
                print("")


def findway(x, y):
    global recursion_count
    recursion_count += 1
    if x == width - 1 and y == height - 1:
        test_maze[x][y] = path
        return True
    elif x < 0 or y < 0 or x >= width or y >= height:
        return False
    elif test_maze[x][y] == wall or test_maze[x][y] == visited:
        return False
    else:
        test_maze[x][y] = visited
        if findway(x - 1, y) or findway(x, y + 1) or findway(x + 1, y) or findway(x, y - 1):
            test_maze[x][y] = path
            return True

        test_maze[x][y] = wrong_path_way
        return False


if __name__ == '__main__':
    print("%% Maze Map %%")
    print("%% pathway: =/ wall: *  %%")
    print("\n")

    printPages()
    findway(0, 0)

    print("")
    print("%% Found Exit!! %%")
    print("%% How can I exit the maze %%")
    print("%% visited: -/ path: O/ wrong_path: X %%")
    print("\n")

    printPages()

    print("\n")
    print("Total Recursion: %d" % recursion_count)
