import time
import sys

sys.setrecursionlimit(100000000)


def iter_way(data, test_number):
    for i in data:
        if data[i] == test_number:
            return i
    return -1


def recursive_way(data, begin, end, test_number):
    if begin >= end:
        return -1
    elif data[begin] == test_number:
        return begin
    else:
        return recursive_way(data, begin + 1, end, test_number)


# divide conquer
def recursive_dc_way(data, begin, end, test_number):
    if begin >= end:
        return -1
    elif data[begin] == test_number:
        return begin
    else:
        mid = int(end / 2)
        if data[mid] == test_number:
            return mid

        indexnum = recursive_way(data, begin, mid - 1, test_number)
        if indexnum != -1:
            return indexnum
        else:
            indexnum = recursive_way(data, mid + 1, end, test_number)
        return indexnum


start_time = time.time()
test_data = [i for i in range(0, 100000000)]
# print(test_data)
#print(iter_way(test_data, len(test_data)))
# print(recursive_way(test_data,  0, len(test_data), len(test_data)/2))
# print(recursive_dc_way(test_data, 0, len(test_data), len(test_data)))

last_time = time.time()

print("\n")
print(last_time - start_time)
