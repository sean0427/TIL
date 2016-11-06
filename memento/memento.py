#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Memento:

    def __init__(self, arg=100, arg2=100):
        self.arg = arg
        self.arg2 = arg2

    def __str__(self):
        return '{} {}'.format(self.arg, self.arg2)

class Originator:

    def __init__(self, memo = Memento()):
        self.memento = memo

    def save(self, memo):
        self.memento = memo

    def load(self):
        return self.memento

    def display_status(self):
        print(self.memento)

class Caretaker:

    def __init__(self, memo = Memento()):
        self.recovery(memo)

    def recovery(self, memo):
        self.memento = memo

    def display_status(self):
        print(self.memento)

if __name__ == "__main__":
    memo = Memento(30, 20)
    print(memo)

    admin = Originator(Memento(10, 20))
    admin.display_status()

    client = Caretaker(admin.load())
    client.display_status()
