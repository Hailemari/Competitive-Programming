import math
import os
import random
import re
import sys


def weirdNum(num):
    if 1 <= num <= 100:
        if num % 2 != 0:
            print("Weird")
        elif num % 2 == 0 and (2 <= num <= 5):
            print("Not Weird")
        elif num % 2 == 0 and (6 <= num <= 20):
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    weirdNum(n)
