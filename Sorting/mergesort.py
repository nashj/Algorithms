#!/usr/bin/env python

from sorting_tests import test

def merge(left_list, right_list):
    # left_list and right_list must be sorted
    sorted_list = []
    while (len(left_list) > 0) or (len(right_list) > 0):
        if (len(left_list) > 0) and (len(right_list) > 0):
            if left_list[0] < right_list[0]:
                sorted_list.append(left_list[0])
                left_list = left_list[1:]
            else:
                sorted_list.append(right_list[0])
                right_list = right_list[1:]
        elif len(left_list) > 0:
            sorted_list.append(left_list[0])
            left_list = left_list[1:]
        else: # right_list nonempty
            sorted_list.append(right_list[0])
            right_list = right_list[1:]
    return sorted_list

def mergesort(list):
    # Lists of length <= 1 are trivially sorted
    if len(list) <= 1:
        return list
    
    # Split the list in half and sort each side
    left_list = mergesort( list[0:len(list)/2] )
    right_list = mergesort( list[len(list)/2:] )
                           
    # Merge the newly sorted lists 
    return merge(left_list, right_list)

if __name__ == "__main__":
    test(mergesort)
