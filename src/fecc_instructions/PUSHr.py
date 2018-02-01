import AbstractMemoryInstruction as AMI


class PUSH(AMI):

    def __init__(self, registry):
        super(AMI, self).__init__(registry)

    def generate(self):
        return 'push %{}'.format(self.value)
