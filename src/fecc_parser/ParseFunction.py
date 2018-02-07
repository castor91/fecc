from fecc_object.FunctionObject import FunctionObject
from fecc_object.EOFObject import EOFObject
from fecc_object.SOFObject import SOFObject
from fecc_object.ReturnObject import ReturnObject
from fecc_object.ConstantObject import ConstantObject
from fecc_object.IdentifierObject import IdentifierObject
from fecc_object.NegationObject import NegationObject
from fecc_object.LogicalNegationObject import LogicalNegationObject
from fecc_object.BitwiseObject import BitwiseObject
from fecc_object.SemicolonObject import SemicolonObject
from fecc_object.AdditionObject import AdditionObject
from fecc_object.MultiplicationObject import MultiplicationObject
from fecc_object.DivisionObject import DivisionObject
from fecc_object.LogicalOrObject import LogicalOrObject
from fecc_object.LogicalAndObject import LogicalAndObject
from fecc_object.EqObject import EqObject
from fecc_object.GteObject import GteObject
from fecc_object.GtObject import GtObject
from fecc_object.LteObject import LteObject
from fecc_object.LtObject import LtObject
from fecc_object.NeqObject import NeqObject

from fecc_tokens.Identifier import Identifier
from fecc_tokens.Return import Return
import fecc_tokens.Paren as Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Semicolon import Semicolon
from fecc_tokens.Negation import Negation
from fecc_tokens.LogicalNegation import LogicalNegation
from fecc_tokens.Bitwise import Bitwise
from fecc_tokens.UnOp import UnOp
from fecc_tokens.BinOp import BinOp
from fecc_tokens.Addition import Addition
from fecc_tokens.Multiplication import Multiplication
from fecc_tokens.Division import Division
from fecc_tokens.LogicalOr import LogicalOr
from fecc_tokens.LogicalAnd import LogicalAnd
from fecc_tokens.Eq import Eq
from fecc_tokens.Gte import Gte
from fecc_tokens.Gt import Gt
from fecc_tokens.Lte import Lte
from fecc_tokens.Lt import Lt
from fecc_tokens.Neq import Neq

from fecc_exceptions.ParserException import ParserException
import FirstParser as FP


#Stage 1
def parse_function(type, tokens):
    name = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(name, Identifier):
        raise ParserException(Identifier, name)
    name = IdentifierObject(name)
    params = parse_params(tokens)
    lbrace = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(lbrace, Paren.LBrace):
        raise ParserException(Paren.LBrace, lbrace)

    statements = parse_statements(tokens)

    rbrace = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(rbrace, Paren.RBrace):
        raise ParserException(Paren.RBrace, rbrace)

    return FunctionObject((type, name, params, statements))


def parse_EOF(tokens):
    return EOFObject(tokens)


def parse_SOF(tokens):
    return SOFObject(tokens)


def parse_params(tokens):
    lparen = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(lparen, Paren.LParen):
        raise ParserException(Paren.LParen, lparen)

    #TODO params
    params = []

    rparen = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(rparen, Paren.RParen):
        raise ParserException(Paren.RParen, rparen)
    return params


def parse_statements(tokens):
    statements = []
    current = FP.FirstParser.pop_next_token(tokens)
    if isinstance(current, Return):
        statements.append(parse_return(tokens))
    else:
        raise ParserException(Return, current)

    return statements


def parse_return(tokens):
    return_statement = ReturnObject(parse_expression(tokens))
    next_token = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(next_token, Semicolon):
        raise ParserException(Semicolon, next_token)
    return return_statement


def parse_constant(constant, tokens):
    if not isinstance(constant, Constant):
        raise ParserException(Constant, constant)
    return ConstantObject(constant)


#Stage 2
#<exp> ::= <logical-and-exp> { "||" <logical-and-exp> }
def parse_expression(tokens):
    first = parse_logical_and(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, LogicalOr):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_logical_and(tokens)
        first = LogicalOrObject(first, second)

        symbol = FP.FirstParser.get_next_token(tokens)

    return first

#<term> ::= <factor> { ("*" | "/") <factor> }
def parse_term(tokens):
    first = parse_factor(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, Multiplication) or isinstance(symbol, Division):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_factor(tokens)
        if isinstance(symbol, Multiplication):
            first = MultiplicationObject(first, second)
        else:
            first = DivisionObject(first, second)

        symbol = FP.FirstParser.get_next_token(tokens)

    return first

#<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
def parse_factor(tokens):
    next_token = FP.FirstParser.pop_next_token(tokens)
    if isinstance(next_token, Paren.LParen):
        return_expression = parse_expression(tokens)
        next_token = FP.FirstParser.pop_next_token(tokens)
        if isinstance(next_token, Paren.RParen):
            return return_expression

        raise ParserException(Paren.RParen, next_token)

    elif isinstance(next_token, UnOp):
        return parse_UnOp(next_token, tokens)
    elif isinstance(next_token, Constant):

        return parse_constant(next_token, tokens)
    elif isinstance(next_token, Semicolon):
        return SemicolonObject(tokens)

    raise ParserException('Factor', next_token)


def parse_UnOp(token, tokens):
    if isinstance(token, Negation):
        return parse_negation(tokens)
    elif isinstance(token, LogicalNegation):
        return parse_logical_negation(tokens)
    elif isinstance(token, Bitwise):
        return parse_bitwise(tokens)

    raise ParserException(UnOp, token)


def parse_negation(tokens):
    return NegationObject(parse_factor(tokens))


def parse_bitwise(tokens):
    return BitwiseObject(parse_factor(tokens))


def parse_logical_negation(tokens):
    return LogicalNegationObject(parse_factor(tokens))

#Stage 3
'''
def parse_BinOp(token, tokens):
    if isinstance(token, Addition):
        return parse_addition(tokens)
    elif isinstance(token, Multiplication):
        return parse_multiplication(tokens)
    elif isinstance(token, Division):
        return parse_division(tokens)

    raise ParserException(BinOp, token)


def parse_addition(tokens):
    raise NotImplemented()


def parse_multiplication(tokens):
    raise NotImplemented()


def parse_division(tokens):
    raise NotImplemented()
'''
#Stage 4
#<logical-and-exp> ::= <equality-exp> { "&&" <equality-exp> }
def parse_logical_and(tokens):
    first = parse_equality(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, LogicalAnd):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_equality(tokens)
        first = LogicalAndObject(first, second)

        symbol = FP.FirstParser.get_next_token(tokens)

    return first

#<equality-exp> ::= <relational-exp> { ("!=" | "==") <relational-exp> }
def parse_equality(tokens):
    first = parse_relational(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, Neq) or isinstance(symbol, Eq):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_relational(tokens)
        if isinstance(symbol, Neq):
            first = NeqObject(first, second)
        else:
            first = EqObject(first, second)
        symbol = FP.FirstParser.get_next_token(tokens)

    return first

#<relational-exp> ::= <additive-exp> { ("<" | ">" | "<=" | ">=") <additive-exp> }
def parse_relational(tokens):
    first = parse_additive(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, Lte) or isinstance(symbol, Lt) or isinstance(symbol, Gte) or isinstance(symbol, Gt):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_additive(tokens)
        if isinstance(symbol, Lte):
            first = LteObject(first, second)
        elif isinstance(symbol, Lt):
            first = LtObject(first, second)
        elif isinstance(symbol, Gte):
            first = GteObject(first, second)
        else:
            first = GtObject(first, second)

        symbol = FP.FirstParser.get_next_token(tokens)

    return first

#<additive-exp> ::= <term> { ("+" | "-") <term> }
def parse_additive(tokens):
    first = parse_term(tokens)
    symbol = FP.FirstParser.get_next_token(tokens)
    while isinstance(symbol, Addition) or isinstance(symbol, Negation):
        symbol = FP.FirstParser.pop_next_token(tokens)
        second = parse_term(tokens)
        first = AdditionObject(first, second if isinstance(symbol, Addition) else NegationObject(second))

        symbol = FP.FirstParser.get_next_token(tokens)

    return first