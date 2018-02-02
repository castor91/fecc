from AbstractObject import *

class ConstantObject(AbstractObject):

    def __init__(self, value):
        super(ConstantObject, self).__init__(value._value)

    def generate(self, out_code):
        out_code.append(PUSH(self._value))
