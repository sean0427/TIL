#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Handler:

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass

class HandlerA(Handler):
    
    def handle_request(self, request):
        if request < 5:
            print('A Handler', request)
        elif self.successor != None:
            self.successor.handle_request(request)

class HandlerB(Handler):
    
    def handle_request(self, request):
        if request >= 5 and request < 10:
            print('B Handler', request)
        elif self.successor != None:
            self.successor.handle_request(request)


class HandlerC(Handler):
    
    def handle_request(self, request):
        if request:
            print('C Handler', request)

if __name__ == '__main__':
    handler_a = HandlerA()    
    handler_b = HandlerB()    
    handler_c = HandlerC()

    handler_a.set_successor(handler_b)
    handler_b.set_successor(handler_c)

    for request in 1, 2, 6, 7, 8, 10 ,20:
        handler_a.handle_request(request)
