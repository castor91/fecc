import AbstractMemoryInstruction as AMI


class POP(AMI):

    def __init__(self, registry):
        super(AMI, self).__init__(registry)

    def generate(self):
        return 'pop %{}'.format(self.value)
