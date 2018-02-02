from AbstractMemoryInstruction import AbstractMemoryInstruction as AMI


class POP(AMI):

    def __init__(self, registry):
        super(POP, self).__init__(registry)

    def generate(self):
        return 'pop %{}'.format(self._value)
