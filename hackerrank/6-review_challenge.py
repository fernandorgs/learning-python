#!/bin/python3
T = int(input())
if (T >= 1) and (T <= 10):
    for j in list(range(T)):
        S = list(input())
        if (len(S) >= 2) and (len(S) <= 10000):
            even = ""
            odd = ""
            for i in range(len(S)):
                if (i % 2) == 0:
                    even = even+S[i]
                else:
                    odd = odd+S[i]
            print(even,odd)
        else:
            print("word must have 2-10000 chars.")
else:
    print("only 1-10 interations allowed.")
