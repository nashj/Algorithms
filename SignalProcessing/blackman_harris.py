#!/usr/bin/env python

import math

def blackman_harris(size):
    # Generalization of Hamming family
    # Minimizes side-lobe levels

    a0 = .35875
    a1 = .48829
    a2 = .14128
    a3 = .01168
    window = []
    for n in range(0,size):
        window.append(a0 - a1*math.cos((2*math.pi*n)/(size-1)) + a2*math.cos((4*math.pi*n)/(size-1)) - a3*math.cos((6*math.pi*n)/(size-1)))
    return window

if __name__ == "__main__":
    print blackman_harris(16)
