class SOFObject:
    def __init__(self):
        pass

    def generate(self, output_file):
        output_file.write('.globl main\n')

    def __str__(self):
        return ''