#!/usr/bin/python3.4

def decorator(method):
    def wrapper():
        print('before')
        method()
        print('after')
    return wrapper 

def con():
    print('doSomeThing')

if __name__ == "__main__":
    @decorator
    con()
