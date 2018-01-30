class Type():
    def __init__(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def __str__(self):
        return 'TYPE {}'.format(self._type)