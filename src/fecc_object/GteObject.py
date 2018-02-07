from AbstractObject import *

class GteObject(AbstractObject):

    def __init__(self, value1, value2):
        super(GteObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
