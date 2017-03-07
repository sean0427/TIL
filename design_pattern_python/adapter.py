#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Adaptee:
    def do_something(self):
        print('Target to something')

class Adapter:

    def __init__(self, target):
        if target == None:
            raise Exception('Adapter', 'Error Target')

        self.adaptee = target

    def do_something(self):
        self.adaptee.do_something();

if __name__ == "__main__":
    adapter = Adapter(Adaptee())
    adapter.do_something()
