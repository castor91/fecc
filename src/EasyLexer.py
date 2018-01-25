import re
from tokens.Identifier import Identifier
from tokens.Constant import Constant
from tokens.Paren import Paren
from tokens.Semicolon import Semicolon
#from exceptions.LexerException import LexerException

class EasyLexer:
    def __init__(self, input_string):
        self._input = input_string
        self._tokens = []

    def lex(self):
        local_input = self._input
        string_regex = r'^[ |\n]*([a-zA-Z][a-zA-Z0-9_]*)'
        number_regex = r'^[ |\n]*([1-9][0-9]*|0)'
        paren_regex = r'^[ |\n]*(\(|\)|\[|\]|{|})'
        semicolon_regex = r'^[ |\n]*(;)'

        string_regex_compiled = re.compile(string_regex)
        number_regex_compiled = re.compile(number_regex)
        paren_regex_compiled = re.compile(paren_regex)
        semicolon_regex_compiled = re.compile(semicolon_regex)

        while len(local_input) > 0:
            token = re.match(string_regex_compiled, local_input)
            if token:
                #self._tokens.append((token.group()))
                self._tokens.append(Identifier(token.group()))
                local_input = local_input[token.end():]
                continue

            token = re.match(number_regex_compiled, local_input)
            if token:
                #self._tokens.append((token.group()))
                self._tokens.append(Constant(token.group()))
                local_input = local_input[token.end():]
                continue

            token = re.match(paren_regex_compiled, local_input)
            if token:
                #self._tokens.append((token.group()))
                self._tokens.append(Paren(token.group()))
                local_input = local_input[token.end():]
                continue

            token = re.match(semicolon_regex_compiled, local_input)
            if token:
                #self._tokens.append((token.group()))
                self._tokens.append(Semicolon())
                local_input = local_input[token.end():]
                continue

            else:
                print 'Error {}'.format(local_input)
                #raise LexerException(local_input)
                break

        return self._tokens