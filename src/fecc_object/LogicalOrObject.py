from AbstractObject import *

class LogicalOrObject(AbstractObject):

    def __init__(self, value1, value2):
        super(LogicalOrObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
