#!/bin/python3

import math
import os
import random
import re
import sys

# Longest Common Subsequence
def longestCommonSubsequence(a, b):
    n_of_cols = len(a)+2
    n_of_rows = len(b)+2
    subseqs = [[(0,'') if i==1 or j==1 else a[i] if i==0 else b[j] if j==0 else None for j in range(n_of_cols)] for i in range(n_of_rows)]

    for i in range(2, n_of_rows):
        for j in range(2, n_of_cols):
            if b[i-2] == a[j-2]:
                subseqs[i][j] = (subseqs[i-1][j-1][0] + 1, 'NW')
            elif subseqs[i][j-1][0] > subseqs[i-1][j][0]:
                subseqs[i][j] = (subseqs[i][j-1][0], 'W')
            else:
                subseqs[i][j] = (subseqs[i-1][j][0], 'N')
    fptr = open('out_test02.txt', 'w')
    fptr.write('Test #2: \n\n')
    fptr.write('\n'.join([''.join(['{:10}'.format(str(item)) for item in row]) for row in subseqs]))
    fptr.close()
    lcs = []
    get_lcs(subseqs, b, n_of_rows-1, n_of_cols-1, lcs)
    return [' '.join(map(str, lcs))]

def get_lcs(dp_matrix, word, i, j, result):
    if i<2 or j<2:
        return ''
    if dp_matrix[i][j][1] == 'NW':
        get_lcs(dp_matrix, word, i-1, j-1, result)
        result.append(word[i-2])
        return result
    elif dp_matrix[i][j][1] == 'N':
        get_lcs(dp_matrix, word, i-1, j, result)
    else:
        get_lcs(dp_matrix, word, i, j-1, result)

