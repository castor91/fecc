from AbstractObject import AbstractObject as AO

class NegationObject(AO):

    def __init__(self, value):
        super(NegationObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append('pop %eax')
        out_code.append('neg %eax')
        out_code.append('push %eax')
