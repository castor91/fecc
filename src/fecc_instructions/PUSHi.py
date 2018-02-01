import AbstractMemoryInstruction as AMI


class PUSH(AMI):

    def __init__(self, value):
        super(AMI, self).__init__(value)

    def generate(self):
        return 'push ${}'.format(self._value)
