from AbstractObject import *

class ReturnObject(AbstractObject):

    def __init__(self, value):
        super(ReturnObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)

        out_code.append(POP('eax'))
        out_code.append(RET())
