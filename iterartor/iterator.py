#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Iterator:

    def __init__(self,collection):
        self.collection = collection
        self.index = 0

    def first(self):
        self.index = 0 

    def next(self):
        if self.is_done():
            raise 'Over index'

        self.index += 1
        return self.index

    def get_current_item(self):
        return self.collection[self.index]

    def is_done(self):
        return self.index == len(self.collection)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6, 7]
    interator = Iterator(list_a)

    while(not interator.is_done()):
        print(interator.get_current_item())
        interator.next()
