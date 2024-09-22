#!/bin/python3

import math
import os
import random
import re
import sys

# array size n
# shift elements of the array by a given number of rotations 
# (%) module operation is a workaround to troubleshoot the error when the index goes beyond the end of the list
# i.e. rotations=2, size of the arr = 5
# when dividing 3 by 5 give 0 as the integer part because 3 is smaller than 5. So in the case of (i + 2) % 5 The remainder is 3 because 5 does not fit into 3 at alll

def rotateLeft(d, arr):
    new_arr=[]
    size = len(arr)
    new_arr=[0] * size
    for i in range(size):
        new_arr[i] = arr[(i + d) % size] 
    return new_arr
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
