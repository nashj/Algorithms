#!/usr/bin/env python

import math

def hamming(size):
    # Applies Hamming window to the samples
    alpha = .54
    beta = 1 - alpha

    window = []
    for n in range(0,size):
        window.append(alpha - beta*math.cos(2*math.pi*n/(size-1)))
    return window

if __name__ == "__main__":
    print hamming(8)
