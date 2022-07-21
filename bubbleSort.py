import math
import os
import random
import re
import sys




def countSwaps(lst):
    if 2 <= n <= 600:
        
        numOfSwaps = 0
        
        for i in range(n):
            if 1 <= a[i] <= 2000000:
               
                curSwaps = 0

                for j in range(0, n - 1):
                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
                      
                        curSwaps += 1
                        
                numOfSwaps += curSwaps
                        
                if curSwaps == 0:
                    break
                
        print("Array is sorted in " + str(numOfSwaps) + " swaps.")
        print("First Element: " + str(a[0]))
        print("Last Element: " + str(a[-1]))

   
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))