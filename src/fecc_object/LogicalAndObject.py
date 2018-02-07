from AbstractObject import *

class LogicalAndObject(AbstractObject):

    def __init__(self, value1, value2):
        super(LogicalAndObject, self).__init__()

    def generate(self, out_code):
        raise NotImplementedError()
