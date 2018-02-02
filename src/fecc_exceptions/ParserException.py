class ParserException(Exception):

    def __init__(self, expected, token):
        self._expected = expected
        self._token = token

    def __str__(self):
        return '{} error: expected {} but {} found.'.format(self.__class__.__name__, self._expected, self._token.__class__.__name__)
