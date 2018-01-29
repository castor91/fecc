import re
from fecc_tokens.Type import Types
from fecc_tokens.Keyword import Keyword
from fecc_tokens.Paren import Symbols
from fecc_tokens.Constant import Constant
from fecc_tokens.Identifier import Identifier
#from fecc_exceptions.LexerException import LexerException


class RegexLexer:

    def __init__(self, input_string):
        self._input = input_string
        self._tokens = []
        self._tokensEnum = [Keyword, Types, Symbols]

    def lex(self):
        local_input = self._input
        identifier_regex = r'[a-zA-Z][a-zA-Z0-9_]*'
        number_regex = r'[1-9][0-9]*|0'
        identifier_regex_compiled = re.compile(identifier_regex)
        number_regex_compiled = re.compile(number_regex)

        regex = r'(' + identifier_regex + ')|(' + number_regex + ')|({)|(})|(;)|(\()|(\))'
        regex_compiled = re.compile(regex)
        print re.findall(regex_compiled, local_input)
        for m in re.finditer(regex_compiled, local_input):
            token_string = m.group()
            print '={}='.format(token_string)
            token = ([cls.get(token_string) for cls in self._tokensEnum if cls.has(token_string)])
            if token:
                self._tokens.append(token)
            elif re.match(identifier_regex_compiled, token):
                self._tokens.append(Identifier(token))
            elif re.match(number_regex_compiled, token):
                self._tokens.append(Constant(token))
            else:
                #raise LexerException.LexerException(token)
                pass

        return self._tokens
