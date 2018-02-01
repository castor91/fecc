from AbstractObject import AbstractObject as AO

class EOFObject(AO):

    def __init__(self, value):
        super(EOFObject, self).__init__(value)

    def generate(self, out_code): pass
