class LexerException():

    def __init__(self, input):
        self._input = input

    def __str__(self):
        return 'Unkown token {}'.format(self._input)
