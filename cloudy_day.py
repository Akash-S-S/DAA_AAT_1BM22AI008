#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)
    m = len(y)
    
    events = []
    for i in range(n):
        events.append((x[i], 0, i)) 
    
    for i in range(m):
        events.append((y[i] - r[i], -1, i))  
        events.append((y[i] + r[i], 1, i))   
    
    events.sort()

    active_clouds = set()
    will_add = {}
    ans = 0
    
    for event in events:
        pos, typ, idx = event
        
        if typ == 1:  
            active_clouds.remove(idx)
        elif typ == -1:
            active_clouds.add(idx)
        else:  
            if len(active_clouds) == 0:
                ans += p[idx]
            elif len(active_clouds) == 1:
                only_cloud = next(iter(active_clouds))
                if only_cloud not in will_add:
                    will_add[only_cloud] = 0
                will_add[only_cloud] += p[idx]
    
    max_add = 0
    for val in will_add.values():
        if val > max_add:
            max_add = val
    
    return ans + max_add
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
