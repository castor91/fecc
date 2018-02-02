from AbstractObject import *

class TypeObject(AbstractObject):

    def __init__(self, value):
        super(TypeObject, self).__init__(value.get_type())

    def generate(self, out_code): pass
