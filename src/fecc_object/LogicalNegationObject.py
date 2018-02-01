class LogicalNegationObject:
    def __init__(self, value):
        self._value = value

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append('pop %eax\n')
        out_code.append('cmpl $0, %eax\n')
        out_code.append('movl $0, %eax\n')
        out_code.append('sete %al\n')
        out_code.append('push %eax\n')

    def __str__(self):
        return 'NOT {}'.format(str(self._value))
