from AbstractBinOpInstruction import AbstractBinOpInstruction as ABOI


class iMUL(ABOI):

    def __init__(self, registry1, registry2):
        super(iMUL, self).__init__(registry1, registry2)

    def generate(self):
        return 'imul %{}, %{}'.format(self._registry1, self._registry2)
