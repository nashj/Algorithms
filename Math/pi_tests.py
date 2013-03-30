#!/usr/bin/env python

import math

def test(piFxn):
    diff = piFxn() - math.pi
    assert(diff < 1.0e-15)
    print "Tests passed!"
