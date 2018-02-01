from AbstractObject import AbstractObject as AO

class TypeObject(AO):

    def __init__(self, value):
        super(TypeObject, self).__init__(value.get_type())

    def generate(self, out_code): pass
