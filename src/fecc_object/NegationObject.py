class NegationObject:
    def __init__(self, value):
        self._value = value

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append('pop %eax\n')
        out_code.append('neg %eax\n')
        out_code.append('push %eax\n')

    def __str__(self):
        return 'NEG {}'.format(str(self._value))
