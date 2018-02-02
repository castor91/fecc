from AbstractMemoryInstruction import AbstractMemoryInstruction as AMI


class PUSH(AMI):

    def __init__(self, value, is_registry=False):
        super(PUSH, self).__init__(value)
        self._is_registry = is_registry

    def generate(self):
        return 'push {}{}'.format('%' if self._is_registry else '$', self._value)
