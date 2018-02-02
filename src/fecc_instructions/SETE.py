from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETE(AGI):

    def __init__(self, value):
        super(SETE, self).__init__(value)

    def generate(self):
        return 'sete %{}'.format(self._value)
