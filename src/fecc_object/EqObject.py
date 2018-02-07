from AbstractObject import *

class EqObject(AbstractObject):

    def __init__(self, value1, value2):
        super(EqObject, self).__init__((value1, value2))

    def generate(self, out_code):
        self._value[0].generate(out_code)
        self._value[1].generate(out_code)
        out_code.append(POP('eax')) #Second
        out_code.append(POP('ecx')) #First
        out_code.append(CMPL('eax', 'ecx', is_registry=True))
        out_code.append(MOVL(0, 'eax'))
        out_code.append(SETE('al'))
        out_code.append(PUSH('eax', is_registry=True))
