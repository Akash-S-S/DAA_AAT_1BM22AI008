#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#old

def stringConstruction(s):
    # Write your code here
    visited_map = {}
    
    for char in s:
        if char not in visited_map:
            visited_map[char] = 1
        
    unique_chars = 0
    for val in visited_map.values():
        unique_chars += 1
        
    return unique_chars
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
