#import re
from tokens.Types import Types
from tokens.Keyword import Keyword


class Lexer:

    def __init__(self, input_string):
        self._input = input_string.replace('\n', ' ').split(' ')
        self._tokens = []
        self._tokensEnum = [Keyword, Types]

    def lex(self):
        for token in self._input:
            self._tokens.append([cls.get(token) for cls in self._tokensEnum if cls.has(token)])



            '''
            if token == 'int': self._tokens.append(Int())
            elif token == 'return': self._tokens.append((Return()))

            else: #or identifier or number
                identifier = r'^[a-zA-Z][a-zA-Z0-9_]*$'
                number = r'^[1-9][0-9]*$'
                ident_re = re.compile(identifier)
                numb_re = re.compile(number)
                if ident_re.match(token): self._tokens.append(Identifier)
                elif numb_re.match(token): self._tokens.append(Number)
            '''



        return self._tokens
