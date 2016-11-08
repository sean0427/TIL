#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Receiver:

    def action(self):
        print('do action')

class Command:

    def __init__(self, receiver):
        self.receiver = receiver

    def excute(self):
        self.receiver.action()

class Invoker:

    def __init__(self):
        self.queue = [] 

    def add_command(self, command):
        self.queue.append(command)

    def excute_all(self):
        for command in self.queue:
            command.excute()

if __name__ == '__main__':
    receiver = Receiver()
    command = Command(receiver)
    invoker = Invoker()
    invoker.add_command(command)
    invoker.excute_all()
