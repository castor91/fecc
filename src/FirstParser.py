class FirstParser:

    def __init__(self):
        print '[+] Parser {}'.format(self.__class__.__name__)

    def parse(self, tokens):
        while len(tokens) > 0:
            current = tokens.pop()

            break
