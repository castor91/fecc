from AbstractBinOpInstruction import AbstractBinOpInstruction as ABOI


class AND(ABOI):

    def __init__(self, registry1, registry2):
        super(AND, self).__init__(registry1, registry2)

    def generate(self):
        return 'and %{}, %{}'.format(self._registry1, self._registry2)
