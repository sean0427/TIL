#!/usr/bin/env python
# -*- conding: utf-8 -*- 

def heapify(array, i, heap_size):
    largest = i 
    while largest <= len(array):
        first = largest
        left = 2 * first + 1
        right = 2 * first + 2

        if right < heap_size and array[right] > array[largest]:
            largest = right 

        if left < heap_size and array[left] > array[largest]:
            largest = left 

        if largest is not first:
            temp = array[first]
            array[first] = array[largest]
            array[largest] = temp
        else:
            return

def build_max_heap(array):
    for i in range(len(array) - 1, -1, -1):
        heapify(array, i, len(array))

def heapsort(array):
    build_max_heap(array)
    heap_size = len(array)

    for i in range(len(array) - 1, 0, -1):
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        heap_size -= 1
        heapify(array, 0, heap_size)

if __name__ == '__main__':
    a = [3, 2, 9, 1, 20, 10]
    heapsort(a)
    print(a)
