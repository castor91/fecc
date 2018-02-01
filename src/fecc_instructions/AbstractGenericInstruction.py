from abc import ABCMeta, abstractmethod


class AbstractGenericInstruction:
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self._value = value

    @abstractmethod
    def generate(self):
        pass

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__.upper(), self._value)
