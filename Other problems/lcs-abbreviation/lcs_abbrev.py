#!/bin/python3

import math
import os
import random
import re
import sys



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

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result, '\n\n')


