import math
import os
import random
import re
import sys
import time
from lcs import lcs

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = lcs.longestCommonSubsequence(a, b)
    with open("output02.txt", encoding="utf-8") as file:
        x = [l.strip() for l in file]
    print(x)

    print(result)
