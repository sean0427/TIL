#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Handler:
    pass

class HandlerA(Handler):
    pass

class HandlerA(Handler):
    pass



if __name__ == '__main__':
    handler_a = HandlerA()    
    handler_b = HandlerB()    
    handler_c = HandlerC()

    handler_a.setSuccessor(handler_b)
    handler_b.setSuccessor(handler_c)

    for request in 1, 2, 6, 7, 8, 10 ,20:
        h1.handleRequest(request)
