from AbstractUnOpInstruction import AbstractUnOpInstruction as AUOI


class NEG(AUOI):

    def __init__(self, registry):
        super(NEG, self).__init__(registry)

    def generate(self):
        return 'neg %{}'.format(self._registry)
