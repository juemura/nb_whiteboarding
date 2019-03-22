#!/bin/python3

import math
import os
import random
import re
import sys
import time
import itertools

def countInversions(arr):
    size = len(arr)
    temp = [None]*size
    count = merge_sort(arr, temp, 0, size-1)
    return count

def merge_sort(arr, temp, left_start, right_end):
    if left_start >= right_end:
        return 0
    middle = (left_start+right_end)//2
    count = merge_sort(arr, temp, left_start, middle)
    count += merge_sort(arr, temp, middle+1, right_end)
    count += merge(arr, temp, left_start, middle, right_end)
    return count

def merge(arr, temp, left_start, middle, right_end):
    index = left_start
    left = left_start
    right = middle+1
    left_end = middle
    count = 0
    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1
        else:
            temp[index] = arr[right]
            right += 1
            count += left_end+1 - left
        index += 1
    if left_end+1-left>0:
        temp[index:index+left_end+1-left] = itertools.islice(arr, left, left_end+1)
    else:
        temp[index:index+right_end+1-right] = itertools.islice(arr, right, right_end+1)
    arr[left_start:right_end + 1] = itertools.islice(temp, left_start, right_end + 1)
    return count

