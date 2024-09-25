#!/bin/python3

import math
import os
import random
import re
import sys

# Left-to-Right Diagonal, goes from the top-left corner to the bottom-right corner
# The elements on this diagonal are located at positions where the row index equals the column index i.e., arr[i][i] n = 3
# When i = 0: it accesses arr[0][0] (first row, first column), When i = 1: it accesses arr[1][1] (second row, second column), etc.
# Right-to-Left Diagonal, goes from the top-right corner to the bottom-left corner
# The elements on this diagonal are located at positions where for each row index i, the corresponding column index for 
# the right-to-left diagonal is calculated as n - i - 1
# When i = 0: it accesses arr[0][n- i -1]--> n - 0 - 1 (first row, last column)
# When i = 0: it accesses arr[0][n- i -1]--> n - 1 - 1 (first row, second to last column)
# 
#

def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    size = len(arr) 
    for i in range(size):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][size - i - 1]
    return abs(left_to_right_diagonal - right_to_left_diagonal)
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
