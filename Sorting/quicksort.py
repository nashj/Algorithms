#!/usr/bin/env python

from sorting_tests import test

def quicksort(list):
    # Lists of length 1 or 0 are trivially sorted
    if len(list) <= 1:
        return list

    # Break the list into two smaller lists by comparing each value with the first element in the list, called the pivot. 
    pivot = list[0]
    lteq_list = []
    gt_list = []

    for i in list[1:]:
        if i <= pivot:
            lteq_list.append(i)
        else:
            gt_list.append(i)
    
    return quicksort(lteq_list) + [pivot] + quicksort(gt_list)

if __name__ == "__main__":
    test(quicksort)
