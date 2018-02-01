from AbstractObject import AbstractObject as AO

class ReturnObject(AO):

    def __init__(self, value):
        super(ReturnObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append('pop %eax'.format(self._value))
        out_code.append('ret')
