#!/bin/python3
T = int(input())
for j in list(range(T)):
    S = list(input())
    even = ""
    odd = ""
    for i in range(len(S)):
        if (i % 2) == 0:
            even = even+S[i]
        else:
            odd = odd+S[i]
    print(even,odd)
