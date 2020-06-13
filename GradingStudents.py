import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for x in range(len(grades)):
        if(grades[x] > 37):
            if((grades[x] % 5) != 0):
                if(5-(grades[x] % 5) < 3):
                    grades[x] += 5 - (grades[x] % 5)
    return(grades)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
