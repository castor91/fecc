from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETGE(AGI):

    def __init__(self, value):
        super(SETGE, self).__init__(value)

    def generate(self):
        return 'setge %{}'.format(self._value)
