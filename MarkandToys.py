#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices.sort()
    toys = 0
    for price in prices:
        if price <= k:
            k -= price
            toys += 1
        else:
            break

    return toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
