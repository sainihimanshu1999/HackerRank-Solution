
import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    x = 0
    for i in range(len(word)):
        if(x < h[ord(word[i])-97]):
            x = h[ord(word[i])-97]
    return x*len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
