class Paren:
    def __init__(self, paren):
        self._paren = paren

    def __str__(self):
        return 'PAREN {}'.format(self._paren)
