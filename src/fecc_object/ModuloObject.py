from AbstractObject import *

class ModuloObject(AbstractObject):

    def __init__(self, value1, value2):
        super(ModuloObject, self).__init__((value1, value2))

    def generate(self, out_code):
        self._value[0].generate(out_code)
        self._value[1].generate(out_code)
        out_code.append(MOVL(0, 'edx'))
        out_code.append(POP('ecx'))
        out_code.append(POP('eax'))
        out_code.append(iDIV('ecx'))
        out_code.append(PUSH('edx', is_registry=True))
