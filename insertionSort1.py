import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    
    num = arr[-1]
    leftIndex = n-2

    while (num < arr[leftIndex]) and (leftIndex >= 0):
        arr[leftIndex+1] = arr[leftIndex]
        print(*arr)
        leftIndex -=1

    arr[leftIndex+1] = num
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)