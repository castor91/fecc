from AbstractObject import AbstractObject as AO

class SOFObject(AO):

    def __init__(self, value):
        super(SOFObject, self).__init__(value)

    def generate(self, out_code):
        out_code.append('.globl main')
