#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Composite:

    def __init__(self, name):
        self.children = {}
        self.name = name

    def add(self, name, node):
        if name is None:
            raise ('not input name')
        
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
    compositeA = Composite('A')
    compositeA.display()

    compositeB = Composite('B')
    compositeA.add('B', compositeB)
    compositeB.add('leafB', Leaf('leafB'))
    compositeA.add('leaf', Leaf('leaf'))
    compositeA.display()

    compositeB.remove('leafB')
    compositeB.display()

    compositeA.display()
