from AbstractObject import *

class GtObject(AbstractObject):

    def __init__(self, value1, value2):
        super(GtObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
