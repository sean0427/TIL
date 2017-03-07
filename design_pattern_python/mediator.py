#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Mediator:

    def __init__(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2

    def send(self, message, colleague):
        if colleague is colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)

class Colleague1:

    def __init__(self):
        self.name = 'A'

    def notify(self, message):
        print(self.name, message)


class Colleague2:

    def __init__(self):
        self.name = 'B'

    def notify(self, message):
        print(self.name, message)

if __name__ == '__main__':
    colleague1 = Colleague1()
    colleague2 = Colleague2()
    mediator = Mediator(colleague1, colleague2)
    mediator.send('A send message', colleague1)
    mediator.send('B send message', colleague2)
