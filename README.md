# DAA_AAT_1BM22AI008

# Name: Akash S.S
# USN: 1BM22AI008
# Section: 4A
# Subject: DAA AAT HackerRank



# 1. Knapsack

#!/bin/python3

import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    # Write your code here
    dp = [0] * (k + 1)

    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    
    return dp[k]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    results = []

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        results.append(result)

    for result in results:
        fptr.write(str(result) + '\n')

    fptr.close()



# 2. Cloudy Day

#!/bin/python3

import math
import os
import random
import re
import sys

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



# 3. QuickSort 1 - Partition
   
#!/bin/python3

import math
import os
import random
import re
import sys

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high 
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def qs(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        qs(arr, low, p-1)
        qs(arr, p+1, high)
    

def quickSort(arr):
    # Write your code here
    n = len(arr)
    qs(arr, 0, n-1)
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



# 4. String Construction

#!/bin/python3

import math
import os
import random
import re
import sys

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

