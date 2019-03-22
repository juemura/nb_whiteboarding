import math
import os
import random
import re
import sys
import time
import merge_sort_leftright as ms_slice
import merge_sort_temp as ms_temp
import merge_sort_islice as ms_islice



if __name__ == '__main__':
    fptr = open('out_test11.txt', 'w')

    fptr.write('Test #11: \n\n')
    with open("output/output11.txt", encoding="utf-8") as file:
        x = [l.strip() for l in file]

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = []
        arr2 = []
        arr3 = []
        for line in input().rstrip().split():
            arr.append(int(line))
            arr2.append(int(line))
            arr3.append(int(line))

        # print(arr)
        start_time = time.time()
        result1 = ms_slice.countInversions(arr)        
        assert(str(result1) == x[t_itr])
        fptr.write("---Using slice %s seconds ---\n" % (time.time() - start_time))
        
        start_time = time.time()
        result2 = ms_temp.countInversions(arr2)
        assert(str(result2) == x[t_itr])
        fptr.write("---Using temp %s seconds ---\n" % (time.time() - start_time))

        start_time = time.time()
        result3 = ms_islice.countInversions(arr3)        
        assert(str(result3) == x[t_itr])
        fptr.write("---Using temp/islice %s seconds ---\n\n" % (time.time() - start_time))
    fptr.close()