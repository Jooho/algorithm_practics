import random
import sys

import time

sys.setrecursionlimit(100000000)

def iter_way(data, find_max=True):
    max_min_number = 0
    for i in range(len(data)):
        if find_max & data[i - 1] < data[i]:
            max_min_number = data[i]
        elif not find_max & data[i - 1] > data[i]:
            max_min_number = data[i]
        else:
            pass
    return max_min_number

def recursive_way(data,begin,end):
    if begin==end:
        return data[begin]
    else:
        return max(recursive_way(data,begin+1,end),data[begin])

test_data = [ random.randrange(0,10) for i in range(0, 10)]
test_data.append(0)
print(test_data)
start_time = time.time()
print(iter_way(test_data,False))
# print(recursive_way(test_data,0,len(test_data)-1))
last_time = time.time()

print("\n")
print(last_time - start_time)
