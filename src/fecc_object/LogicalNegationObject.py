from AbstractObject import *

class LogicalNegationObject(AbstractObject):

    def __init__(self, value):
        super(LogicalNegationObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append(POP('eax'))
        out_code.append(CMPL(0, 'eax'))
        out_code.append(MOVL(0, 'eax'))
        out_code.append(SETE('al'))
        out_code.append(PUSH('eax', is_registry=True))
