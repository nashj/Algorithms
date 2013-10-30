#!/usr/bin/env python

import random
import math

if __name__ == "__main__":
    total_samples = 100000
    inside_count = 0

    for i in range(0,total_samples):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if ((x**2 + y**2) <= 1):
            inside_count += 1


    print "Area of the circle should be ", math.pi*.5*.5
    print "Area of the circle, according to rejection sampling, is: ", 1.0*inside_count/total_samples

