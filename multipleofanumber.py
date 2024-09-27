#!/bin/python3

import math
import os
import random
import re
import sys



# Prints Fizz, Buzz or FizzBuzz depending on if the number is multipe of 3 and 5, 3 or 5 or neither
# 
#
# 
#

def fizzBuzz(n):
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif (i % 3 == 0) and (i % 5 != 0):
            print('Fizz')
        elif (i % 3 != 0) and (i % 5 == 0):
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
