#!/bin/python

import sys
from math import log10, trunc

def b2_to_b10(n):
    m = n - trunc(n)
    n -= m
    digitCount = trunc(log10(n) + 1)
    sum = 0
    for i in range(1, digitCount + 1):
        sum += ((n%10**i - n%10**(i-1)) / 10**(i-1)) * 2**(i - 1)
    return sum

def b10_to_b2(n):
    m = []
    while (n > 1):
        m.append(str(int(n%2)));
        n//=2
    m.append(str(int(n)))
    m.reverse()
    return ''.join(m)

        

# print(b2_to_b10(float(sys.argv[1])))
# print(b10_to_b2(float(sys.argv[1])))
