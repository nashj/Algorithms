#!/usr/bin/env python

import math
from pi_tests import test

def borwein():
    # 1985 version
    a1 = 6 - 4 * math.sqrt(2)
    y1 = math.sqrt(2) - 1
    a0 = 1.0
    
    k = 0
    while (a1 - a0 != 0):
        #print k
        #print a1
        a0 = a1
        y0 = y1

        y1 = (1 - (1 - y0**4)**(1/4)) / (1 + (1 - y0**4)**(1/4))
        a1 = a0 * (1 + y1)**4 - 2**(2*k+3) * y1 * (1 + y1 + y1**2)
        k += 1

    return 1.0/a1

if __name__ == "__main__":
    test(borwein)
