#!/usr/bin/python3.4

from abc import ABCMeta

class Abc(metaclass=ABCMeta):
    pass

Abc.register(tuple)

assert issubclass(set, Abc)
assert issubclass(tuple, Abc)
assert isinstance((), Abc)
