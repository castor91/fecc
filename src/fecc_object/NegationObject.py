from AbstractObject import *

class NegationObject(AbstractObject):

    def __init__(self, value):
        super(NegationObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append(POP('eax'))
        out_code.append(NEG('eax'))
        out_code.append(PUSH('eax', is_registry=True))
