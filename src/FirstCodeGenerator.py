class FirstCodeGenerator:

    def __init__(self):
        print '[+] Code Generator {}'.format(self.__class__.__name__)

    @staticmethod
    def generate(optimized_code, out_code):
        for code in optimized_code:
            code.generate(out_code)