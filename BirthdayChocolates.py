

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    ways = 0
    for i in range(len(s)):
        n = 0
        count = 0
        while(n < (m)):
            count += s[i+n]
            n += 1
        if(count == d):
            ways += 1
        if(i+n == len(s)):
            break
    return ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
