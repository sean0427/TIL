#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Product:
    
    def __init__(self):
        self.parts = list()

    def add(self, part):
        self.parts.append(part)

    def show(self):
        for part in self.parts:
            print(part)

class Builder:

    def build_part_a(self):
        raise('a not implement');

    def build_part_b(self):
        raise('b not implement');

class ConcreteBuilder1(Builder):
    
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("1-a")

    def build_part_b(self):
        self.product.add("1-b")

    def get_result(self):
        return self.product

class ConcreteBuilder2(Builder):
    
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("2-a")

    def get_result(self):
        return self.product

def director(builder):
    builder.build_part_a()
    builder.build_part_b()

if __name__ == '__main__':
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()

    director(b1)
    try :
        director(b2)
    except:
        print('build build2 error')

    p1 = b1.get_result()

    try :
        p2 = b2
    except:
        print('build2 error')

    p1.show()
