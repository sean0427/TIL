#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Subject:

    def request(self):
        print("real quest")

class Proxy:
    
    def __init__(self):
        self.real_subject = Subject()

    def request(self):
        self.real_subject.request()

if __name__ == '__main__':
    proxy = Proxy()
    proxy.request()
