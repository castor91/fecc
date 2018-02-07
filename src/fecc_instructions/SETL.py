from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETL(AGI):

    def __init__(self, value):
        super(SETL, self).__init__(value)

    def generate(self):
        return 'setl %{}'.format(self._value)
