from AbstractCompareInstruction import AbstractCompareInstruction as ACI


class CMPL(ACI):

    def __init__(self, value1, value2, is_registry=False):
        super(CMPL, self).__init__(value1, value2)
        self._is_registry = is_registry

    def generate(self):
        return 'cmpl {}{}, %{}'.format('%' if self._is_registry else '$', self._value1, self._value2)
