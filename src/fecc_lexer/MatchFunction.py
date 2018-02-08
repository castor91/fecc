from fecc_tokens import *

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
def logical_and_match(word):
    return LogicalAnd() if word == '&&' else BitwiseAnd()

def logical_or_match(word):
    return LogicalOr() if word == '||' else  BitwiseOr()

def eq_match(_):
    return Eq()


def neq_match(_):
    return Neq()


def lte_match(word):
    return Lte() if word == '<=' else Lt()


def gte_match(word):
    return Gte() if word == '>=' else Gt()


def modulo_match(_):
    return Modulo()


def logical_negation_neq_match(word):
    return logical_negation_match(word) if word == '!' else neq_match(word)