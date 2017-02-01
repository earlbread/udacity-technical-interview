#!/usr/bin/env python

def mergesort(array):
    pass

if __name__ == '__main__':
    import random
    array = [random.randint(-10, 10) for _ in range(10)]
    print("Before: ", array)
    array = mergesort(array)
    print("After: ", array)
