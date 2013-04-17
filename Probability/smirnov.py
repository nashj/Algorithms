#!/usr/bin/env python

import random

class InverseSampler:
    def __init__(self, inverse_cdf):
        self.inverse_cdf = inverse_cdf
    def sample(self):
        return self.inverse_cdf(random.uniform(0,1))


if __name__ == "__main__":
    # Testing the exponential distribution
    # The CDF for the exp dist is 1 - exp(-lamba*x),
    # so the inverse CDF is -ln(1-y)/x

    import math
    lamb = 5
    inverseCDF = lambda x: -math.log(1-x)/lamb
    inverseSampler = InverseSampler(inverseCDF)
    sum_x = 0
    sum_x2 = 0
    iterations = 100000
    for i in range(0,iterations):
        sample = inverseSampler.sample()
        sum_x += sample
        sum_x2 += sample*sample

    mean = sum_x / iterations
    variance = sum_x2 / iterations - math.pow(sum_x / iterations,2)
    
    assert(abs(mean - 1.0/lamb) < .01)
    assert(abs(variance - 1.0/lamb/lamb) < .001)

    print "Exponential distribution with lambda =", lamb
    print "Mean is", mean
    print "Variance is", variance
