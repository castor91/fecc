class NegationObject:
    def __init__(self, value):
        self._value = value

    def generate(self, output_file):
        self._value.generate(output_file)
        output_file.write('pop %eax\n')
        output_file.write('neg %eax\n')
        output_file.write('push %eax\n')

    def __str__(self):
        return 'NEG {}'.format(str(self._value))
