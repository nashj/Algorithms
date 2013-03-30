#!/usr/bin/env python

import math
from pi_tests import test

def gaussLegendre():
    pi_old = 1.0
    pi_new = 2.0

    a0 = 1.0
    b0 = 1.0/math.sqrt(2)
    t0 = .25
    p0 = 1.0
    
    while (pi_new - pi_old != 0):
        pi_old = pi_new
        a1 = (a0 + b0)/2.0
        b1 = math.sqrt(a0 * b0)
        t1 = t0 - p0 * (a0 - a1)**2
        p1 = 2*p0
    
        a0 = a1
        b0 = b1
        t0 = t1
        p0 = p1
    
        pi_new = (a0 + b0)**2 / (4 * t0)
        # print pi_new
    return pi_new
    
if __name__ == "__main__":
    test(gaussLegendre)
