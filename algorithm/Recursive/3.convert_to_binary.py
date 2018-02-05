from multiprocessing import Queue
import time

q = Queue()


def iter_way(original_number):
    quotient_number = original_number
    global q
    while quotient_number > 2:
        q.put(int(quotient_number % 2))
        quotient_number = quotient_number / 2

    for i in range(q.qsize()):
        print(q.get(), end="")


def recursive_way(quotient_number):

    if quotient_number < 2:
        return
    else:
        print(int(quotient_number % 2),end="")
        recursive_way(quotient_number / 2)

test_number = 100000000000000000000000000000
# 시간 재기
start_time = time.time()

# iter_way(test_number)
recursive_way(test_number)

last_time = time.time()


print("\n")
print(last_time - start_time)

