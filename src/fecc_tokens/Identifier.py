class Identifier:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._name)
