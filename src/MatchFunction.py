from fecc_tokens.Semicolon import Semicolon
from fecc_tokens.Paren import Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Identifier import Identifier
from fecc_tokens.Type import Type
from fecc_tokens.Return import Return
from fecc_tokens.EOF import EOF


def string_match(word):
    if word == 'int':
        return Type(word)
    elif word == 'return':
        return Return()

    return Identifier(word)


def number_match(word):
    return Constant(word)


def paren_match(word):
    return Paren(word)


def semicolon_match(_):
    return Semicolon()


def eof_match(_):
    return EOF()
