from AbstractObject import AbstractObject as AO

class FunctionObject(AO):

    def __init__(self, value): # value = (type_obj, name, params, statements)
        #super(FunctionObject, self).__init__(value)
        self._type = value[0]
        self._name = value[1]
        self._params = value[2]
        self._statements = value[3]

    def generate(self, out_code):
        out_code.append('{}:\n'.format(self._name.get_name()))
        for stats in self._statements:
            stats.generate(out_code)

    def __str__(self):
        stats = ['\n\t' + str(x) for x in self._statements]
        return 'FUN {} {}:\n' \
               '\tparams: ({})\n' \
               '\tbody:' \
               '\t\t{}\n'.format(self._type, self._name, ', '.join(self._params), '\n\t\t'.join(stats))
