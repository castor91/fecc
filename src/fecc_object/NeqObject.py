from AbstractObject import *

class NeqObject(AbstractObject):

    def __init__(self, value1, value2):
        super(NeqObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
