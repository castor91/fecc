class NegationObject:
    def __init__(self, value):
        self._value = value

    def generate(self, output_file):
        self._value.generate()
        output_file.write('pop %eax\n')
        output_file.write('neg %eax\n')

    def __str__(self):
        return 'NEG'
