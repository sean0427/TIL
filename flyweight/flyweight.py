#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Flyweight:
    
    def __init__(self, name=''):
        self.name = name

    def operation(self):
        print(self.name)

class FlyweightFactory:

    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, name):
        if name not in self.flyweights:
            self.flyweights[name] = Flyweight(name)
        return self.flyweights[name]

if __name__ == '__main__':
    factory = FlyweightFactory();

    flyweight_a = factory.get_flyweight('A');
    flyweight_b = factory.get_flyweight('B');

    flyweight_a.operation();
    flyweight_b.operation();
