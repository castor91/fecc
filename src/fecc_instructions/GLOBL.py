import AbstractGenericInstruction as AGI


class GLOBL(AGI):

    def __init__(self, value):
        super(GLOBL, self).__init__(value)

    def generate(self):
        return '.globl {}'.format(self._value)
