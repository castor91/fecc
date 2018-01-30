class ReturnObject:
    def __init__(self, value):
        self._value = value

    def generate(self, output_file):
        self._value.generate(output_file)
        output_file.write('pop %eax\n'.format(self._value))
        output_file.write('ret\n')

    def __str__(self):
        return '{} -> {}'.format(self.__class__.__name__, self._value)