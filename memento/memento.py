#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Memento:

    def __init__(self, hp=100, mp=100):
        self.hp = hp
        self.mp = mp

    def __str__(self):
        return '{} {}'.format(self.hp, self.mp)

class Originator:

    def __init__(self, memo = Memento()):
        self.memento = memo

    def save(self, memo):
        self.memento = memo

    def load(self):
        return self.memnto

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

    admin = Originator()
    client = Caretaker()
