from AbstractCompareInstruction import AbstractCompareInstruction as ACI


class CMPL(ACI):

    def __init__(self, value1, value2):
        super(CMPL, self).__init__(value1, value2)

    def generate(self):
        return 'cmpl ${}, %{}'.format(self._value1, self._value2)
