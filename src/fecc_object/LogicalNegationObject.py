from AbstractObject import AbstractObject as AO

class LogicalNegationObject(AO):

    def __init__(self, value):
        super(LogicalNegationObject, self).__init__(value)

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append(POP('eax'))
        out_code.append(CMPL(0, 'eax'))
        out_code.append(MOVL(0, 'eax'))
        out_code.append(SETE('al'))
        out_code.append(PUSHr('eax'))
        '''
        out_code.append('pop %eax\n')
        out_code.append('cmpl $0, %eax\n')
        out_code.append('movl $0, %eax\n')
        out_code.append('sete %al\n')
        out_code.append('push %eax\n')
        '''