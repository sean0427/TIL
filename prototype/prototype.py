#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Prototype:

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def clone(self):
        prototype = Prototype()
        prototype.set_name(self.name)
        prototype.set_number(self.number)
        return prototype

    def print_all(self):
        print('name {}'.format(self.name))
        print('number {}'.format(self.number))

if __name__ == "__main__":
    proto = Prototype()
    proto.set_name('a')
    proto.set_number(1)

    proto2 = proto.clone()

    proto.print_all()
    proto2.print_all()

    print(proto)
    print(proto2)
