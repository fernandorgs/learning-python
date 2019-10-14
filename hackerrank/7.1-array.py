#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    count = 0
    reverse = []
    separator = " "
    n = int(input())
    if n >= 1 and n <= 1000:
        pos = n - 1
        arr = list(map(int, input().rstrip().split()))
        while count != n:
            reverse.append(arr[pos])
            count = count + 1
            pos = pos - 1
        print(separator.join(map(str, reverse)))
    else:
        print("must be between 1 and 1000.")
