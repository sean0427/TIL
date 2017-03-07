#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Abstraction:
    
    def __init__(self, implementor):
        self.implementor = implementor

    def opration(self):
        self.implementor.operation()

class Implementor:

    def operation():
       print('implementor 1')

class ImplementorB:

    def operation():
        print('B')

if __name__ == '__main__':
    abstraction = Abstraction(Implementor)
    abstraction.opration()

    abstraction = Abstraction(ImplementorB)
    abstraction.opration()
