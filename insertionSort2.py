import math
import os
import random
import re
import sys


def arrayAsInt(arr):
        cha=""
        for number in arr:
            cha += str(number) + " "
        print(cha)

def insertionSort2(n, arr):
    for i in range(n):
        j = i;
        while (j > 0 and arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
        if (i != 0):
            arrayAsInt(arr)
            
    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
