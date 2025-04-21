import random
import time
# Implementation of binary search algorithm in Python

# we will prove that binary search u=is faster than naive search

# niave search: scan entire list and ask if it is equal to the target
#if yes, return the index of the target
# if no, return -1

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

    
# binary search: divide the list in half and check if the target is in the left or right half
# if yes, repeat the process until the target is found
# if no, return -1
def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
        if high is None:
            high = len(l) - 1

    if high < low:
            return -1

    # example l = [1, 3, 5, 10, 12] # return = 3
    mid_point = (low + high) // 2 # 2

    if l[mid_point] == target:
        return mid_point
    elif target < l[mid_point]:
        return binary_search(l, target, low, mid_point - 1)
    else:
        # target > l[mid_point]
        return binary_search(l, target, mid_point + 1, high)
    

if __name__ == "__main__":
    # l = [1, 3, 5, 10, 12]
    # target = 14
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(sorted_list)

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", end - start/length, 'Seconds')
                                
    

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("binary search time: ", end - start/length, 'Seconds')                            



    

