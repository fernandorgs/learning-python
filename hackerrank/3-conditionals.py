#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if (N % 2) != 0:
        print("Weird") #odd
    else: #even
        if (N > 20):
            print("Not Weird")
        else: # even between 2 and 20
            if (N >= 6) and (N <= 20):
                print("Weird")
            else: #2 or 4
                print("Not Weird")
