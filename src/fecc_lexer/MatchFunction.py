from fecc_tokens.Semicolon import Semicolon
from fecc_tokens.Paren import Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Identifier import Identifier
from fecc_tokens.Type import Type
from fecc_tokens.Return import Return
from fecc_tokens.EOF import EOF
from fecc_tokens.Negation import Negation
from fecc_tokens.Bitwise import Bitwise
from fecc_tokens.LogicalNegation import LogicalNegation
from fecc_tokens.Addition import Addition
from fecc_tokens.Multiplication import Multiplication
from fecc_tokens.Division import Division
from fecc_tokens.LogicalAnd import LogicalAnd
from fecc_tokens.LogicalOr import LogicalOr
from fecc_tokens.Eq import Eq
from fecc_tokens.Neq import Neq
from fecc_tokens.Lte import Lte
from fecc_tokens.Lt import Lt
from fecc_tokens.Gte import Gte
from fecc_tokens.Gt import Gt

#Stage 1
def string_match(word):
    if word == 'int':
        return Type(word)
    elif word == 'return':
        return Return()

    return Identifier(word)


def number_match(word):
    if word.startswith('0x'):
        return Constant(word[2:], 16)
    elif word.startswith('0') and len(word) > 1:
        return Constant(word[1:], 8)
    return Constant(word, 10)


def paren_match(word):
    return Paren.getParen(word)


def semicolon_match(_):
    return Semicolon()


def eof_match(_):
    return EOF()

#Stage 2
def negation_match(_):
    return Negation()

def bitwise_match(_):
    return Bitwise()

def logical_negation_match(_):
    return LogicalNegation()


#Stage 3
def addition_match(_):
    return Addition()


def multiplication_match(_):
    return Multiplication()


def division_match(_):
    return Division()

#Stage 4
def logical_and_match(_):
    return LogicalAnd()


def logical_or_match(_):
    return LogicalOr()


def eq_match(_):
    return Eq()


def neq_match(_):
    return Neq()


def lte_match(word):
    return Lte() if word == '<=' else Lt()

def gte_match(word):
    return Gte() if word == '>=' else Gt()
