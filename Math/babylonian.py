#!/usr/bin/env python
import math

def sqrt(S):
    # Babylonian method
    x0 = 0
    x1 = S/1.1
    while (x1 != x0):
        x0 = x1
        x1 = .5 * (x0 + S/x0)
    return x1

if __name__ == "__main__":
    assert(sqrt(9)==math.sqrt(9))
    assert(sqrt(5)==math.sqrt(5))
    assert(sqrt(155)==math.sqrt(155))

