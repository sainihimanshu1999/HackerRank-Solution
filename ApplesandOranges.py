import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    ocount = 0

    for i in range(len(apples)):
        x = a + apples[i]
        if(x in range(s, t+1)):
            acount += 1
    for i in range(len(oranges)):
        y = b + oranges[i]
        if(y in range(s, t+1)):
            ocount += 1
    print(acount)
    print(ocount)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
