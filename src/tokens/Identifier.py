class Identifier:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._name)
