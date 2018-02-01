from abc import ABCMeta, abstractmethod


class AbstractCompareInstruction:
    __metaclass__ = ABCMeta

    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    @abstractmethod
    def generate(self):
        pass

    def __str__(self):
        return '{} {}, {}'.format(self.__class__.__name__.upper(), self._value1, self._value2)
