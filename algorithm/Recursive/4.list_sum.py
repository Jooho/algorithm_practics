

def iter_way(test_list):
    sum=0
    for i in range(len(test_list)):
        sum += test_list[i]

    print(sum)

def recursive_way(test_list, n):
    if n <=0:
        return 0
    else:
        return recursive_way(test_list,n-1) + test_list[n-1]



test_list=[1,2,3,4,5,6,7,8,9,10]
iter_way(test_list)
print(recursive_way(test_list,len(test_list)))