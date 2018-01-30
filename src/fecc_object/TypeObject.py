class TypeObject:
    def __init__(self, type_obj):
        self._type = type_obj.get_type()

    def __str__(self):
        return '{}'.format(self._type.upper())
