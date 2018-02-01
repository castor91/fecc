from first_object.FunctionObject import FunctionObject
from first_object.EOFObject import EOFObject
from first_object.SOFObject import SOFObject
from first_object.ReturnObject import ReturnObject
from first_object.ConstantObject import ConstantObject
from first_object.IdentifierObject import IdentifierObject
from first_object.NegationObject import NegationObject
from first_object.LogicalNegationObject import LogicalNegationObject
from first_object.BitwiseObject import BitwiseObject
from first_object.SemicolonObject import SemicolonObject

from fecc_tokens.Identifier import Identifier
from fecc_tokens.Return import Return
import fecc_tokens.Paren as Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Semicolon import Semicolon
from fecc_tokens.Negation import Negation
from fecc_tokens.LogicalNegation import LogicalNegation
from fecc_tokens.Bitwise import Bitwise

from fecc_exceptions.ParserException import ParserException
import FirstParser as FP


#Stage 1
def parseFunction(type, tokens):
    name = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(name, Identifier):
        raise ParserException(Identifier, name)
    name = IdentifierObject(name)
    params = parseParams(tokens)
    lbrace = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(lbrace, Paren.LBrace):
        raise ParserException(Paren.LBrace, lbrace)

    statements = parseStatements(tokens)

    rbrace = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(rbrace, Paren.RBrace):
        raise ParserException(Paren.RBrace, rbrace)

    return FunctionObject(type, name, params, statements)


def parseEOF():
    return EOFObject()


def parseSOF():
    return SOFObject()


def parseParams(tokens):
    lparen = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(lparen, Paren.LParen):
        raise ParserException(Paren.LParen, lparen)

    #TODO params
    params = []

    rparen = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(rparen, Paren.RParen):
        raise ParserException(Paren.RParen, rparen)
    return params


def parseStatements(tokens):
    statements = []
    current = FP.FirstParser.pop_next_token(tokens)
    if isinstance(current, Return):
        statements.append(parseReturn(tokens))

    return statements


def parseReturn(tokens):
    return_statement = ReturnObject(parseExpression(tokens))
    next_token = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(next_token, Semicolon):
        raise ParserException(Semicolon, next_token)
    return return_statement


def parseConstant(constant, tokens):
    #print 'Parsing', value, tokens
    #constant = FP.FirstParser.pop_next_token(tokens)
    if not isinstance(constant, Constant):
        raise ParserException(Constant, constant)
    return ConstantObject(constant)

#Stage 2
def parseExpression(tokens):
    next_token = FP.FirstParser.pop_next_token(tokens)
    if isinstance(next_token, Constant):
        return parseConstant(next_token, tokens)
    elif isinstance(next_token, Negation):
        return parseNegation(tokens)
    elif isinstance(next_token, LogicalNegation):
        return parseLogicalNegation(tokens)
    elif isinstance(next_token, Bitwise):
        return parseBitwise(tokens)
    elif isinstance(next_token, Semicolon):
        return SemicolonObject(tokens)
    else:
        raise ParserException('Expression', next_token)


def parseNegation(tokens):
    return NegationObject(parseExpression(tokens))


def parseBitwise(tokens):
    return BitwiseObject(parseExpression(tokens))


def parseLogicalNegation(tokens):
    return LogicalNegationObject(parseExpression(tokens))
