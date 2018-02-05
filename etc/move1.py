#!/usr/bin/python
# !python

import sys, os

# Without Enter, get input character
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def call(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            print(ch)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


#test_data
test_data=[[0 for col in range(10)]for row in range(10)]
test_data[0][0]=1 # The initial position of #

# test_data = [
#     [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# ]

height = len(test_data)
width = len(test_data[0])


def printPages(data):
    os.system("clear")
    for i in range(height):
        for j in range(width):
            if test_data[i][j] == 0:
                print("*", end="")
            else:
                print("#", end="")

            if j == width-1:
                print("\n")


def validate_x_position(x):
    if x < 0:
        return 0
    elif x >= height:
        return height - 1
    return x


def validate_y_position(y):
    if y < 0:
        return 0
    elif y >= width:
        return width - 1
    else:
        return y


def move():
    x = 0
    y = 0
    while True:
        printPages(test_data)
        getch = _GetchUnix().call()
        if getch == 'a':
            test_data[x][y] = 0
            y = validate_y_position(y - 1)
            test_data[x][y] = 1

        elif getch == 'd':
            test_data[x][y] = 0
            y = validate_y_position(y + 1)
            test_data[x][y] = 1

        elif getch == 'w':
            test_data[x][y] = 0
            x = validate_x_position(x - 1)
            test_data[x][y] = 1

        elif getch == 's':
            test_data[x][y] = 0
            x = validate_x_position(x + 1)
            test_data[x][y] = 1

        else:
            print("it is not one of `aswd`")
            break


if __name__ == "__main__":
    move()
