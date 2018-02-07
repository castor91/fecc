from AbstractObject import *

class LtObject(AbstractObject):

    def __init__(self, value1, value2):
        super(LtObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
