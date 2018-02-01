from AbstractObject import AbstractObject as AO

class BitwiseObject(AO):

    def __init__(self, value):
        super(BitwiseObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append(POP('eax'))
        out_code.append(NOT('eax'))
        out_code.append(PUSH('eax'))

        '''
        out_code.append('pop %eax\n')
        out_code.append('not %eax\n')
        out_code.append('push %eax\n')
        '''