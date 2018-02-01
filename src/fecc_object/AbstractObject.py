from abc import ABCMeta, abstractmethod

class AbstractObject:
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return '{}{}{}'.format(self.__class__.__name__.upper()[:3], ' ' if self._value is not None else '', self._value)

    @abstractmethod
    def generate(self, out_code):
        pass
