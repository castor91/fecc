import AbstractGenericInstruction as AGI


class NOT(AGI):

    def __init__(self, value):
        super(AGI, self).__init__(value)

    def generate(self):
        return 'sete %{}'.format(self._value)
