#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found.
    Time complexity of n"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    '''time complexity of n'''
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    '''Time complexity of n'''
    if array[index] == item:
        return index
    if index == len(array) - 1:
        return None

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found.
    Time complexity of log(n)"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    lower = 0
    upper = len(array)
    while True:
        mid = ((upper - lower) // 2) + lower # gives us the index of the current middle
        this_item = array[mid]

        if this_item == item:
            break
        if mid == lower or mid == upper:
            return None

        if this_item > item:
            upper = mid
        else:
            lower = mid
    return mid


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left == None:
        left = 0
    if right == None:
        right = len(array)
    
    mid = ((right - left) // 2) + left
    this_item = array[mid]

    if this_item == item:
        return mid
    elif mid == left or mid == right:
        return None

    if this_item > item:
        return binary_search_recursive(array, item, left, mid)
    else:
        return binary_search_recursive(array, item, mid, right)