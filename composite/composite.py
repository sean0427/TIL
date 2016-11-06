#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Composite:

    def __init__(self, name):
        self.children = {}
        self.name = name

    def add(self, name, node):
        if name is None:
            raise('not input name')
        
        self.children[name] = node

    def remove(self, name):
        self.children.pop(name)

    def display(self):
        print (self.name)
        for key in self.children.keys():
            print ('--')
            self.children[key].display()
        print('\n')


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
    composite_a = Composite('A')
    composite_a.display()

    composite_b = Composite('B')
    composite_a.add('B', composite_b)
    composite_b.add('leaf_b', Leaf('leaf_b'))
    composite_a.add('leaf', Leaf('leaf'))
    composite_a.display()

    composite_b.remove('leaf_b')
    composite_b.display()

    composite_a.display()
