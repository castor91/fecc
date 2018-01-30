class FirstCodeGenerator:

    def __init__(self):
        print '[+] Code Generator {}'.format(self.__class__.__name__)


    def generate(self, optimized_code, output_file):
        for code in optimized_code:
            code.generate(output_file)