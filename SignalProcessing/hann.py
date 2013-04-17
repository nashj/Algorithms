#!/usr/bin/env python

import math

def hann(size):
    # Applies Hann window to the samples
    # Side lobes roll off at a 18dB per octave
    window = []
    for n in range(0,size):
        window.append(.5 * (1 - math.cos(2*math.pi*n/(size-1))))
    return window

if __name__ == "__main__":
    print hann(8)
