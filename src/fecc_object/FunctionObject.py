class FunctionObject:

    def __init__(self, type_obj, name, params, statements):
        self._type = type_obj
        self._name = name
        self._params = params
        self._statements = statements

    def generate(self, out_code):
        out_code.append('{}:\n'.format(self._name.get_name()))
        for stats in self._statements:
            stats.generate(out_code)

    def __str__(self):
        stats = ['\n\t'+str(x) for x in self._statements]
        return 'FUN {} {}:\n' \
               '\tparams: ({})\n' \
               '\tbody:' \
               '\t\t{}\n'.format(self._type, self._name, ', '.join(self._params), '\n\t\t'.join(stats))
