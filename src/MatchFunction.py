from tokens.Semicolon import Semicolon
from tokens.Paren import Paren
from tokens.Constant import Constant
from tokens.Identifier import Identifier
from tokens.Type import Type
from tokens.Return import Return
from tokens.EOF import EOF


def string_match( word):
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
