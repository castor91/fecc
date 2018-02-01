class BitwiseObject:
    def __init__(self, value):
        self._value = value

    def generate(self, output_file):
        self._value.generate(output_file)
        output_file.write('pop %eax\n')
        output_file.write('not %eax\n')
        output_file.write('push %eax\n')

    def __str__(self):
        return 'BITW {}'.format(str(self._value))
