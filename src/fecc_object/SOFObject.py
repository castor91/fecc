from AbstractObject import *

class SOFObject(AbstractObject):

    def __init__(self, value):
        super(SOFObject, self).__init__(value)

    def generate(self, out_code):
        out_code.append(GLOBL('main'))

