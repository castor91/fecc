from AbstractUnOpInstruction import AbstractUnOpInstruction as AUOI


class NOT(AUOI):

    def __init__(self, registry):
        super(NOT, self).__init__(registry)

    def generate(self):
        return 'not %{}'.format(self._registry)
