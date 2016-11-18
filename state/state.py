#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Context:

    def __init__(self):
        self.state = State1()
        self.status = 0

    def request(self):
        self.state.handle(self)

    def set_status(self, status):
        self.status = status 

class State1:

    def handle(self, context):
        if context.status < 12:
            print('state1')
        else:
            context.state = State2()

class State2:

    def handle(self, context):
        if context.status < 18:
            print('state2')

if __name__ == '__main__':
    context = Context()

    context.request()
    
    context.set_status(15)

    context.request()
