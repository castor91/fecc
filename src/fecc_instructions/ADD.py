from AbstractBinOpInstruction import AbstractBinOpInstruction as ABOI


class ADD(ABOI):

    def __init__(self, registry1, registry2):
        super(ADD, self).__init__(registry1, registry2)

    def generate(self):
        return 'add %{}, %{}'.format(self._registry1, self._registry2)
