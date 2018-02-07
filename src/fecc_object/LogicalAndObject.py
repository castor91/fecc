from AbstractObject import *

class LogicalAndObject(AbstractObject):

    def __init__(self, value1, value2):
        super(LogicalAndObject, self).__init__((value1, value2))

    def generate(self, out_code):
        self._value[0].generate(out_code)
        self._value[1].generate(out_code)
        out_code.append(POP('eax'))  # Second
        out_code.append(POP('ecx'))  # First
        out_code.append(CMPL(0, 'ecx'))
        out_code.append(SETNE('cl'))
        out_code.append(CMPL(0, 'eax'))
        out_code.append(SETNE('al'))
        out_code.append(AND('cl', 'al'))
        out_code.append(PUSH('eax', is_registry=True))