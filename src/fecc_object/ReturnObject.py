class ReturnObject:
    def __init__(self, value):
        self._value = value

    def generate(self, out_code):
        self._value.generate(out_code)
        out_code.append('pop %eax'.format(self._value))
        out_code.append('ret')

    def __str__(self):
        return 'RETURN {}'.format(self._value)