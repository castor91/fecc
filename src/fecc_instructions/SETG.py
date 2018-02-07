from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class SETG(AGI):

    def __init__(self, value):
        super(SETG, self).__init__(value)

    def generate(self):
        return 'setg %{}'.format(self._value)
