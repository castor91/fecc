from abc import ABCMeta, abstractmethod


class AbstractBinOpInstruction:
    __metaclass__ = ABCMeta

    def __init__(self, registry1, registry2):
        self._registry1 = registry1
        self._registry2 = registry2

    @abstractmethod
    def generate(self):
        pass

    def __str__(self):
        return '{} %{}, %{}'.format(self.__class__.__name__.upper(), self._registry)
