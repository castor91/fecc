class ReturnObject:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return '{} -> {}'.format(self.__class__.__name__, self._value)