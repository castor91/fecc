from AbstractObject import *

class IdentifierObject(AbstractObject):

    def __init__(self, value):
        super(IdentifierObject, self).__init__(value.get_name())

    def generate(self, out_code):
        out_code.append(String(self._value))

    def get_name(self):
        return self._value
