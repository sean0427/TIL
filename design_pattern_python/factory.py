#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class ConcreteA:
    def print_method(self):
        print('a')

class ConcreteB:
    def print_method(self):
        print('b')

class Factory:
    def create(self, type):
        if type is 'a':
            return ConcreteA()
        elif type is 'b':
            return ConcreteB();

if __name__ == '__main__':
    factory = Factory()
    a = factory.create('a')

    try:
        c = factory.create('c')
    except:
        print('factory error')

    a.print_method()
