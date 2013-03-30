#!/usr/bin/env python

def test(sort):
    list1 = [9,5,7,6,1,8,3,4,2]
    sorted_list1 = [1,2,3,4,5,6,7,8,9]
    assert(sort(list1) == sorted_list1)

    list2 = [4,4,4,5,5,5,1,1,1,3,3,3]
    sorted_list2 = [1,1,1,3,3,3,4,4,4,5,5,5]
    assert(sort(list2) == sorted_list2)

    list3 = [9,8,7,6,5,4,3,2,1]
    sorted_list3 = [1,2,3,4,5,6,7,8,9]
    assert(sort(list3) == sorted_list3)

    print "Tests passed!"
