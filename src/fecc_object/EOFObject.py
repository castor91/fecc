class EOFObject:
    def __init__(self):
        pass

    def generate(self, output_file):
        output_file.write('\n')
        output_file.close()

    def __str__(self):
        return ''
