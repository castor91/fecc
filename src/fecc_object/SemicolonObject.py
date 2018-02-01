from AbstractObject import AbstractObject as AO

class SemicolonObject(AO):

    def __init__(self, value):
        super(SemicolonObject, self).__init__(value)

    def generate(self, out_code): pass

    def __str__(self): return ''
