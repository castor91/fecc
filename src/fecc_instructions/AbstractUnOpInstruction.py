from abc import ABCMeta, abstractmethod


class AbstractUnOpInstruction:
    __metaclass__ = ABCMeta

    def __init__(self, registry):
        self._registry = registry

    @abstractmethod
    def generate(self):
        pass

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__.upper(), self._registry)
