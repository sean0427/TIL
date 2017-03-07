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
    
    observer_e = Observer(subject, 'e')
    observer_f = Observer(subject, 'f')

    subject.attach(observer_e)
    subject.notify()

    subject.attach(observer_f)

    subject.detach(observer_e)
    subject.notify()

    try:
        subject.attach(list())
    except Exception as error:
        print(error)

    subject.notify()
