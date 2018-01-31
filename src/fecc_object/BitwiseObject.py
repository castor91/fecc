class BitwiseObject:
    def __init__(self, value):
        self._value = value

    def generate(self, output_file):
        self._value.generate()
        output_file.write('cmpl $0, %eax\n')
        output_file.write('movl $0, %eax\n')
        output_file.write('sete %al\n')

    def __str__(self):
        return ''
