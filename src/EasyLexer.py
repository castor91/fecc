import re
from tokens.EOF import EOF
from tokens.SOF import SOF
import Regex


class EasyLexer:
    def __init__(self, input_string):
        print '[+] Lexer {}'.format(self.__class__.__name__)
        self._input = input_string + '\n' #Add final new line
        self._tokens = [SOF()]

    def lex(self):
        local_input = self._input

        while not isinstance(self._tokens[-1], EOF):
            if len(local_input) == 0:
                print 'Error size 0' #TODO raise exception
                break
            for regex, function_match in Regex.regexs.items():
                token = re.match(regex, local_input)
                if token is not None:
                    self._tokens.append(function_match(token.groups()[1]))
                    local_input = local_input[token.end():]
                    break

        return self._tokens
