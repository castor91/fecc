from AbstractBinOpInstruction import AbstractBinOpInstruction as ABOI


class OR(ABOI):

    def __init__(self, registry1, registry2):
        super(OR, self).__init__(registry1, registry2)

    def generate(self):
        return 'or %{}, %{}'.format(self._registry1, self._registry2)
