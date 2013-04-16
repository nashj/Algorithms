#!/usr/bin/env python

import random
import math

def gaussian():
    pair = gaussianPair()
    return pair[0]

def gaussianPair():
    x = 1
    y = 1
    s = 1
    while (s >= 1):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        s = x**2 + y**2
    ins = math.sqrt(-2.0 * math.log(s) / s)
    g1 = x * ins
    g2 = y * ins
    return g1, g2

if __name__ == "__main__":
    for i in range(0,100):
        print gaussianPair()
