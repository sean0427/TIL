#!/usr/bin/env python
# -*- conding: utf-8 -*- 

def partition(array, p, r):
    x = array[r]
    i = p - 1

    for j in range(p, r, 1) :
        if array[j] <= x:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp 

    temp = array[i+1] 
    array[i+1] = array[r]
    array[r] = temp

    return i + 1

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)

if __name__ == '__main__':
    a = [3, 2, 9, 1, 20, 10]
    quicksort(a, 0, len(a)-1)
    print(a)

