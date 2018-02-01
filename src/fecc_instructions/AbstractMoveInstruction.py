from abc import ABCMeta, abstractmethod


class AbstractMoveInstruction:
    __metaclass__ = ABCMeta

    def __init__(self, src_value, dst_registry):
        self._src_value = src_value
        self._dst_registry = dst_registry

    @abstractmethod
    def generate(self):
        pass

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__.upper(), self._src_value, self._dst_registry)
