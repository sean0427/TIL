#!/usr/bin/env python
# -*- conding: utf-8 -*- 

class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        observers.append(observer)

    def detach(self, observer):
        observers.remove(observer)

    def notify():
        for observer in observers:
            observer.update()
