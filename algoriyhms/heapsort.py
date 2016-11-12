#!/usr/bin/env python
# -*- conding: utf-8 -*- 

def heapsort(array):
    for i in range(len(array) // 2):
        array = heapify(array, i)

def heapify(array, i):
    left = 2*(i+1)-1
    right = 2*(i+1)
    if right <= len(array):
        largest = i
        if array[left] > array[largest]:
            largest = left

        if array[right] > array[largest]:
            largest = right

        if largest is not i:
            temp = array[i]
            array[i] = array[largest]
            array[largest] = temp

    return array

if __name__ == '__main__':
    a = [3, 2, 9]
    a = heapsort(a)
    print(a)
