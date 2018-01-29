class Constant:
    def __init__(self, value, base):
        self._value = value
        self._base = base

    def __str__(self):
        return '{}({}) in base {}'.format(self.__class__.__name__, self._value, self._base)