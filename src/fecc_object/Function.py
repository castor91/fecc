class Function:

    def __init__(self, return_type, name, params, statements):
        self._type = return_type
        self._name = name
        self._params = params
        self._statements = statements

    def __str__(self):
        stats = ['\n\t'+str(x) for x in self._statements]
        return 'FUNCTION:{} {}({}) \n{}\n'.format(self._type, self._name, self._params, ''.join(stats))
