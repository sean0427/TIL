#!/usr/bin/env python
# -*- conding: utf-8 -*- 

from subject import Subject

class Observer:

    def __init__(self, subject, name=None):
        self.name = name
        self.subject = subject

    def update(self):
        print('update observer {}'.format(self.name))

if __name__ == "__main__":
    subject = Subject()

    for name in ['a', 'b', 'c', 'd', 'c']:
        subject.attach(Observer(subject, name))
    
    ob = Observer(subject, "ob")

    subject.attach(ob)
    subject.notify()

    subject.detach(ob)
    subject.notify()
