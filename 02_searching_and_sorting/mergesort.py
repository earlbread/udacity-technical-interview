#!/usr/bin/env python

def merge(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


def mergesort(array):
    if len(array) == 1:
        return array

    mid = len(array) / 2

    a = mergesort(array[:mid])
    b = mergesort(array[mid:])

    return merge(a, b)

if __name__ == '__main__':
    import random
    array = [random.randint(-10, 10) for _ in range(10)]
    print("Before: ", array)
    array = mergesort(array)
    print("After: ", array)
