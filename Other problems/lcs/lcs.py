#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    n_of_cols = len(a)+2
    # print(n_of_cols)
    n_of_rows = len(b)+2
    # print(n_of_rows)
    subseqs = [[(0,'') if i==1 or j==1 else a[i] if i==0 else b[j] if j==0 else None for j in range(n_of_cols)] for i in range(n_of_rows)]
    # for i in range(len(a)):
    #     subseqs[0][i+2] = a[i]
    # for i in range(len(b)):
    #     subseqs[i+2][0] = b[i]
    # print('\n'.join([''.join(['{:10}'.format(str(item)) for item in row]) for row in subseqs]))

    for i in range(2, n_of_rows):
        for j in range(2, n_of_cols):
            # print(i, j)
            # print(b[i-2], a[j-2])
            if b[i-2] == a[j-2]:
                # print(subseqs[i][j])
                subseqs[i][j] = (subseqs[i-1][j-1][0] + 1, 'NW')
                # print(subseqs[i][j])
            elif subseqs[i][j-1][0] > subseqs[i-1][j][0]:
                # print(subseqs[i][j])
                subseqs[i][j] = (subseqs[i][j-1][0], 'W')
                # print(subseqs[i][j])
            else:
                subseqs[i][j] = (subseqs[i-1][j][0], 'N')
            # print('\n'.join([''.join(['{:10}'.format(str(item)) for item in row]) for row in subseqs]))
    # print('\n'.join([''.join(['{:10}'.format(str(item)) for item in row]) for row in subseqs]))
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


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = longestCommonSubsequence(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()