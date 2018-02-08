from src.fecc_exceptions.ParserException import ParserException
from src.fecc_tokens.Type import Type
from src.fecc_tokens.EOF import EOF
from src.fecc_tokens.SOF import SOF
import ParseFunction as PF

from src.fecc_object.TypeObject import TypeObject
from src.fecc_object.EOFObject import EOFObject


class FirstParser:

    def __init__(self):
        print '[+] Parser {}'.format(self.__class__.__name__)
        self._objects = []

    def parseProgram(self, tokens):
        current = FirstParser.pop_next_token(tokens)
        if isinstance(current, SOF):
            self._objects.append(PF.parse_SOF(tokens))
        else:
            raise ParserException(SOF, current)

        while not isinstance(self._objects[-1], EOFObject):
            current = FirstParser.pop_next_token(tokens)

            if isinstance(current, Type): #Function
                self._objects.append(PF.parse_function(TypeObject(current), tokens))
            elif isinstance(current, EOF): #End of file
                self._objects.append(PF.parse_EOF(tokens))

            else:
                raise ParserException('Unknown', current)

        return self._objects

    @staticmethod
    def pop_next_token(tokens):
        token = tokens.pop(0)
        #print 'Next Token: {} {}'.format(token, len(tokens))
        return token

    @staticmethod
    def get_next_token(tokens):
        token = tokens[0]
        return token
