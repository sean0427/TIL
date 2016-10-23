#!/var/python3

from abc import ABCMeta

class SortInterface(metaclass=ABCMeta):

    @abstractmethod
    def sort(self):
        raise 'You are not implement.' 
