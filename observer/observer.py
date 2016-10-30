#!/usr/bin/env python
# -*- conding: utf-8 -*- 

from subject import Subject

class Observer:

    name = None

    def __init__(self, subject ,name):
        self.name = name
        self.subject = subject

    def update():
        print('update observer {}'.format(name))

if __name__ == "__main__":
    subject = Subject()
    subject.attach(Observer(subject, 'A'))
    subject.notify()
