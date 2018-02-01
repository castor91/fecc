import AbstractGenericInstruction as AGI


class RET(AGI):

    def __init__(self):
        super(AGI, self).__init__(None)

    def generate(self):
        return 'ret'
