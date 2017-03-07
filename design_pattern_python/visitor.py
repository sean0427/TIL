#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class ObjectStruct:
    
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

class VisitorA:

    def visitElementA(self, element_a):
        print('A number is', element_a.name)

    def visitElementB(self, element_b):
        print('B number is', element_b.number)

class VisitorB:

    def visitElementA(self, element_a):
        print('A number is', element_a.number)

    def visitElementB(self, element_b):
        print('B name is', element_b.name)

class ElementA:
    
    def __init__(self):
        self.name = 'A'
        self.number = 1

    def accept(self, visitor):
        visitor.visitElementA(self)

class ElementB:
    
    def __init__(self):
        self.name = 'B'
        self.number = 2

    def accept(self, visitor):
        visitor.visitElementB(self)

if __name__ == '__main__':
    struct = ObjectStruct();
    struct.attach(ElementA()) 
    struct.attach(ElementB()) 

    struct.accept(VisitorA())
    struct.accept(VisitorB())
