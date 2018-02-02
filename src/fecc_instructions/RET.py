from AbstractGenericInstruction import AbstractGenericInstruction as AGI


class RET(AGI):

    def __init__(self):
        super(RET, self).__init__(None)

    def generate(self):
        return 'ret'
