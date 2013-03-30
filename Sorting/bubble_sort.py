#!/usr/bin/env python

from sorting_tests import test

def bubble_sort(list):
    swaps_happened = True
    while swaps_happened:
        swaps_happened = False
        for i in range(0, len(list)-1):
            if (list[i] > list[i+1]):
                swap = list[i+1]
                list[i+1] = list[i]
                list[i] = swap
                swaps_happened = True
    return list

if __name__ == "__main__":
    test(bubble_sort)
