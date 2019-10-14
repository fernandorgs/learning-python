#!/bin/python3

import math
import os
import random
import re
import sys

def verifsize(i,minor,major):
    if i >= minor and i <= major:
        return True
    else:
        return False

def revert(array):
    reversed = []
    sizearr = len(array)
    count = 0
    pos = sizearr - 1
    while count != sizearr:
        reversed.append(array[pos])
        count = count + 1
        pos = pos - 1
    return reversed

if __name__ == '__main__':
    n = int(input())
    if verifsize(n,1,1000):
        arr = list(map(int, input().rstrip().split()))
        print(" ".join(map(str, revert(arr))))
    else:
        print("must be between 1 and 1000.")
