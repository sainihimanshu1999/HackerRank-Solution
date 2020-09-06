#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    n = len(arr)
    temp = [0]*n
    return _mergeSort(arr,temp,0,n-1)

def _mergeSort(arr,temp,left,right):
    count = 0

    if left<right:

        mid = (left+right)//2

        count += _mergeSort(arr,temp,left,mid)

        count += _mergeSort(arr,temp,mid+1,right)

        count += merge(arr, temp, left, mid, right)

    return count


def merge(arr,temp,left,mid,right):
    i =left
    j = mid+1
    k = left
    count = 0


    while i<=mid and j <=right:

        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            count += (mid-i+1)
            k+= 1
            j += 1
        
    while i<=mid:
        temp[k]=arr[i]
        k += 1
        i += 1

    while j<= right:
        temp[k] = arr[j]
        k+= 1
        j+= 1


    for x in range(left,right+1):
        arr[x] = temp[x]

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
