from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETNE(AGI):

    def __init__(self, value):
        super(SETNE, self).__init__(value)

    def generate(self):
        return 'setne %{}'.format(self._value)
