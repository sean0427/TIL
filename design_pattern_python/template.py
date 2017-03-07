#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Abstract:
    
    def print_a(self):
        pass

    def print_a(self):
        pass

    def template_method(self):
        self.print_a()
        self.print_b()

class Concrete(Abstract):

    def print_a(self):
        print('conrete implemete A')

    def print_b(self):
        print('conrete implemete B')

if __name__ == '__main__':
    concrete = Concrete()
    concrete.template_method();
