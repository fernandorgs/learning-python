#!/bin/python3

import math
import os
import random
import re
import sys

def verifsize(i,minor,major): #check if a value is within a defined range
    if i >= minor and i <= major:
        return True
    else:
        return False

def revert(array): #invert sequence of array elements
    reversed = []
    sizearr = len(array)
    count = 0
    pos = sizearr - 1
    while count != sizearr:
        reversed.append(array[pos])
        count = count + 1
        pos = pos - 1
    return reversed

def showarray(array): #show array values side by side
    return " ".join(map(str, array))

if __name__ == '__main__':
    n = int(input())
    if verifsize(n,1,1000):
        arr = list(map(int, input().rstrip().split()))
        print(showarray(revert(arr)))
    else:
        print("must be between 1 and 1000.")
