#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    rounded_grades = []
    if 1 <= len(grades) <= 60:
        for i in range(len(grades)):
            if 0 <= grades[i] <= 100:
                if grades[i] < 38:
                    rounded_grades.append(grades[i])
                else:
                    if grades[i] % 5 == 3:
                        rounded_grades.append(grades[i] + 2)
                    elif grades[i] % 5 == 4:
                        rounded_grades.append(grades[i] + 1)
                    else:
                        rounded_grades.append(grades[i])
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
