#!/bin/python3

import math
import os
import random
import re
import sys



#
# If the letter is alphabetically after the preceding letter, it gets transformed to lowercase.
# If the letter is alphabetically before the preceding letter, it gets transformed to uppercase.
# else remains unchanged
# i.e. coOL dog => cOOl dOg

def transformSentence(sentence):
    tranformation=sentence[0]
    for i in range(1, len(sentence)):
        current_value = sentence[i]
        previous_value = sentence[i-1]
        if current_value.lower()<previous_value.lower():
            tranformation += current_value.lower()
        elif current_value.lower()>previous_value.lower():
            tranformation += current_value.upper()
        else:
            tranformation += current_value
    return tranformation
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
