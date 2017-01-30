#!/usr/bin/env python

def partition(array, start, end):
    p = end
    i = start

    while i < p:
        if array[i] > array[p]:
            array[i], array[p - 1] = array[p - 1], array[i]
            array[p], array[p - 1] = array[p - 1], array[p]
            p -= 1
        else:
            i += 1

    return p

def quicksort_helper(array, start, end):
    if end - start < 1:
        return array

    split_point = partition(array, start, end)

    quicksort_helper(array, start, split_point - 1)
    quicksort_helper(array, split_point + 1, end)

    return array

def quicksort(array):
    return quicksort_helper(array, 0, len(array) - 1)

if __name__ == '__main__':
    import random

    array = [random.randint(-10, 10) for _ in range(10)]
    print("Before: ", array)
    array = quicksort(array)
    print("After: ", array)
