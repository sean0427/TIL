#!/usr/bin/env python
# -*- conding: utf-8 -*- 

def heapsort(array):
    for i in range(len(array)-1, -1, -1):
        heapify(array, i)

def heapify(array, i):
    largest = i 
    while largest <= len(array):
        first = largest
        left = 2 * first + 1
        right = 2 * first + 2

        if right < len(array) and array[right] > array[largest]:
            largest = right 

        if left < len(array) and array[left] > array[largest]:
            largest = left 

        if largest is not first:
            temp = array[first]
            array[first] = array[largest]
            array[largest] = temp
        else:
            return

if __name__ == '__main__':
    a = [3, 2, 9, 1, 20, 10]
    heapsort(a)
    print(a)
