from AbstractObject import *

class EqObject(AbstractObject):

    def __init__(self, value1, value2):
        super(EqObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
