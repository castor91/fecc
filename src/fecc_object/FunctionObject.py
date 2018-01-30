class FunctionObject:

    def __init__(self, return_type, name, params, statements):
        self._type = return_type
        self._name = name
        self._params = params
        self._statements = statements

    def generate(self, output_file):
        output_file.write('{}:\n'.format(self._name.get_name()))
        for stats in self._statements:
            stats.generate(output_file)

    def __str__(self):
        stats = ['\n\t'+str(x) for x in self._statements]
        return 'FUNCTION:{} {}({}) \n{}\n'.format(self._type, self._name, self._params, ''.join(stats))
