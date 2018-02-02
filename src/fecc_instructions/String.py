from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class String(AGI):

    def __init__(self, value):
        super(String, self).__init__(value)

    def generate(self):
        return '{}:'.format(self._value)
