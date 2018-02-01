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

from fecc_tokens.Identifier import Identifier
from fecc_tokens.Return import Return
import fecc_tokens.Paren as Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Semicolon import Semicolon
from fecc_tokens.Negation import Negation
from fecc_tokens.LogicalNegation import LogicalNegation
from fecc_tokens.Bitwise import Bitwise
from fecc_tokens.UnOp import UnOp

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
def parse_expression(tokens):
    next_token = FP.FirstParser.pop_next_token(tokens)
    if isinstance(next_token, UnOp):
        return parse_UnOp(next_token, tokens)
    elif isinstance(next_token, Constant):
        return parse_constant(next_token, tokens)
    elif isinstance(next_token, Semicolon):
        return SemicolonObject(tokens)

    raise ParserException('Expression', next_token)


def parse_UnOp(token, tokens):
    if isinstance(token, Negation):
        return parse_negation(tokens)
    elif isinstance(token, LogicalNegation):
        return parse_logical_negation(tokens)
    elif isinstance(token, Bitwise):
        return parse_bitwise(tokens)

    raise ParserException(UnOp, token)


def parse_negation(tokens):
    return NegationObject(parse_expression(tokens))


def parse_bitwise(tokens):
    return BitwiseObject(parse_expression(tokens))


def parse_logical_negation(tokens):
    return LogicalNegationObject(parse_expression(tokens))
