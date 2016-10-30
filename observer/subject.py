#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Subject:

    def __init__(self):
        self.observers = list()

    def attach(self, observer):
        if hasattr(observer, 'update'):
            self.observers.append(observer)
        else:
            raise Exception('Subject', 'Error observer')

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()
