from AbstractBinOpInstruction import AbstractBinOpInstruction as ABOI


class iDIV(ABOI):

    def __init__(self, dst):
        super(iDIV, self).__init__(dst, None)

    def generate(self):
        return 'idivl %{}'.format(self._registry1)

