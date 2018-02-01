from AbstractObject import AbstractObject as AO

class ConstantObject(AO):

    def __init__(self, value):
        super(ConstantObject, self).__init__(value._value)

    def generate(self, out_code):
        out_code.append(PUSHi(self._value))

        '''
        out_code.append('push ${}'.format(self._value))
        '''