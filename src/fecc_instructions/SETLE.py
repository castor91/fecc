from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETLE(AGI):

    def __init__(self, value):
        super(SETLE, self).__init__(value)

    def generate(self):
        return 'setle %{}'.format(self._value)
