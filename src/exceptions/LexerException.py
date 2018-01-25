class LexerException(Exception):
    def __init__(self, token):
        self._token = token

    def __str__(self):
        return 'Token \'{}\' not recognized.'.format(self._token)