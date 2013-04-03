#!/usr/bin/env python
import random
import math

def gaussian():
    pair = gaussianPair()
    return pair[0]

def gaussianPair():
    # Box-Muller Transform
    theta = 2 * math.pi * random.uniform(0,1)
    r = math.sqrt(-2 * math.log(random.uniform(0,1)))
    z0 = r * math.cos(theta)
    z1 = r * math.sin(theta)
    return z0, z1

def first_moment(samples):
    import operator
    return reduce(operator.add, samples, 0) / len(samples)

def second_moment(samples):
    import operator
    return reduce(operator.add, map(lambda x: math.pow(x,2), samples), 0) / len(samples)

def sample_variance(samples):
    # Unbiased sample variance
    # (n/(n-1)) * (E[x^2] - E[x]^2)
    import math
    n = len(samples)
    return (n/(n-1)) * (second_moment(samples) - math.pow(first_moment(samples), 2))

if __name__ == "__main__":
    # Estimate sample point moments
    samples = []
    for i in range(0,10000):
        samples.append(gaussian())
    print samples
    print "Mean:", first_moment(samples)
    print "Variance", sample_variance(samples)
