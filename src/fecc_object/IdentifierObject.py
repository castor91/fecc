from AbstractObject import AbstractObject as AO

class IdentifierObject(AO):

    def __init__(self, value):
        super(IdentifierObject, self).__init__(value.get_name())

    def generate(self, out_code): pass

    def get_name(self):
        return self._value
