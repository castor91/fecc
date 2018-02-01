class SOFObject:
    def __init__(self):
        pass

    def generate(self, out_code):
        out_code.append('.globl main')

    def __str__(self):
        return ''