class IdentifierObject:

    def __init__(self, identifier_object):
        self._name = identifier_object._name

    def get_name(self):
        return self._name

    def __str__(self):
        return '{} -> {}'.format(self.__class__.__name__, self._name)
