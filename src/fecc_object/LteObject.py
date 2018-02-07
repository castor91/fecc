from AbstractObject import *

class LteObject(AbstractObject):

    def __init__(self, value1, value2):
        super(LteObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
