#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class SubSystemA:

    def method_a(self):
        print('subsystem_A')

class SubSystemB:

    def method_b(self):
        print('subsystem_B')

class SubSystemC:

    def method_c(self):
        print('subsystem_C')

class SubSystemD:

    def method_d(self):
        print('subsystem_D')

class Facade:
    
    def __init__(self):
        self.a = SubSystemA()
        self.b = SubSystemB()
        self.c = SubSystemC()
        self.d = SubSystemD()

    def method_1(self):
        self.a.method_a();
        self.d.method_d();

    def method_2(self):
        self.b.method_b();
        self.c.method_c();

if __name__ == '__main__':
    facade = Facade()
    print('1')
    facade.method_1()
    print('2')
    facade.method_2()
