class ConstantObject:
    def __init__(self, value):
        self._value = value._value
        self._base = value._base

    def generate(self, output_file):
        output_file.write('push ${}\n'.format(self._value))

    def __str__(self):
        return '<{}, {}>'.format(self._value, self._base)
