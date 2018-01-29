class LexerException():

    def __init__(self, input):
        self._input = input

    def __str__(self):
        return 'Unknown input {}'.format(self._input)
