#!/bin/python3

import math
import os
import random
import re
import sys
import time


def countInversions(arr):
    return merge_sort(arr)

def merge_sort(arr):
    count = 0
    s = len(arr)
    if s > 1:
        middle = s//2
        left = arr[:middle]
        right = arr[middle:]
        count += merge_sort(left) + merge_sort(right) + merge(arr, left, right)
    return count

def merge(arr, left, right):
    l, r, index = 0, 0, 0
    l_size = len(left)
    r_size = len(right)
    count = 0
    while l < l_size and r < r_size:
        if left[l] <= right[r]:
            arr[index] = left[l]
            l += 1
        else:
            count += l_size - l
            arr[index] = right[r]
            r += 1
        index += 1
    if left[l:]:
        arr[index:] = left[l:]
    else:
        arr[index:] = right[r:]
    return count


# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     fptr = open('output.txt', 'w')

#     t = int(input())

#     for t_itr in range(t):
#         n = int(input())

#         arr = list(map(int, input().rstrip().split()))
        
#         start_time = time.time()
#         result = countInversions(arr)
#         print("--- %s seconds ---" % (time.time() - start_time))

#         fptr.write(str(result) + '\n')

#     fptr.close()
