#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
# def abbreviation(a, b):
#     # print("new word")
#     rows, cols = len(a)+1, len(b)+1
#     if cols > rows or (cols-1 < sum(x.isupper() for x in a)):
#         return 'NO'
#     m = [[0 for _ in range(cols)] for _ in range(rows)]
#     impossible = False
#     # j2 = 1
#     for i in range(1, rows):
#         # print('a letter: ', a[i-1])        
#         if a[i-1].isupper():
#             # if a[i-1] != b[j2-1]:
#             #     return 'NO'           
#             impossible = True
#         for j in range(1, cols):
#             # print('b letter: ', b[j-1])
#             if a[i-1].upper() == b[j-1]:        
#                 m[i][j] = m[i-1][j-1] + 1
#                 impossible = False
#                 # if j == j2:
#                 #     j2 += 1
#             else:
#                 m[i][j] = max(m[i][j-1], m[i-1][j])
#         if impossible:
#             return 'NO'
#     return 'YES' if m[rows-1][cols-1] == cols-1 else 'NO'



def abbreviation(a, b):
    rows, cols = len(a)+1, len(b)+1
    m = [[True if j==0 and i==0 else False for j in range(cols)] for i in range(rows)]
    for i in range(1, rows):
        m[i][0] = m[i-1][0] and a[i-1].islower()
    for i in range(1, rows):
        for j in range(1, cols):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1]
            elif a[i-1].upper() == b[j-1]:
                m[i][j] = m[i-1][j-1] or m[i-1][j]
            elif a[i-1].islower():
                m[i][j] = m[i-1][j]
    if m[rows-1][cols-1]:
        return 'YES'
    return 'NO'




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result, '\n\n')

    # fptr.close()

