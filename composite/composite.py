#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Composite:

    def __init__(self, name):
        self.children = {}
        self.name = name

    def add(self, name, node):
        if name is none:
            raise ('not input name')
        
        self.children[name] = node

    def remove(self, name):
        self.children.pop(name)

    def display(self):
        print (self.name)
        for key in self.children.keys():
            print ('--' + key)
            self.children[key].display()


class Leaf(Composite):

    def __init__(self, name):
        self.name = name

    def add(self):
        raise ('Leaf can\'t add')

    def remove(self):
        raise ('Leaf can\'t add')

    def display(self):
        print('--' + self.name)

if __name__ == '__main__':
    compositeA = Composite('A')
    compositeA.display()
