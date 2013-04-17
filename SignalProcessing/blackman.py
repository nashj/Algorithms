#!/usr/bin/env python

import math

def blackman(size):
    # Applies Hann window to the samples
    # Side lobes roll off at a 18dB per octave
    alpha = .16
    a0 = (1-alpha)/2
    a1 = .5
    a2 = alpha/2
    window = []
    for n in range(0,size):
        window.append(a0 - a1*math.cos((2*math.pi*n)/(size-1)) + a2*math.cos((4*math.pi*n)/(size-1)))
    return window

if __name__ == "__main__":
    print blackman(8)
