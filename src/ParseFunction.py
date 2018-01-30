from fecc_object.FunctionObject import FunctionObject
from fecc_object.EOFObject import EOFObject
from fecc_object.SOFObject import SOFObject
from fecc_object.ReturnObject import ReturnObject
from fecc_object.ConstantObject import ConstantObject
from fecc_object.IdentifierObject import IdentifierObject

from fecc_tokens.Identifier import Identifier
from fecc_tokens.Return import Return
import fecc_tokens.Paren as Paren
from fecc_tokens.Constant import Constant
from fecc_tokens.Semicolon import Semicolon

from fecc_exceptions.ParserException import ParserException
import FirstParser as FP

def parseFunction(type, tokens):
    name = FP.FirstParser.get_next_token(tokens)
    if not isinstance(name, Identifier):
        raise ParserException(Identifier, name)
    name = IdentifierObject(name)
    params = parseParams(tokens)
    lbrace = FP.FirstParser.get_next_token(tokens)
    if not isinstance(lbrace, Paren.LBrace):
        raise ParserException(Paren.LBrace, lbrace)

    statements = parseStatements(tokens)

    rbrace = FP.FirstParser.get_next_token(tokens)
    if not isinstance(rbrace, Paren.RBrace):
        raise ParserException(Paren.RBrace, rbrace)

    return FunctionObject(type, name, params, statements)


def parseEOF():
    return EOFObject()


def parseSOF():
    return SOFObject()


def parseParams(tokens):
    lparen = FP.FirstParser.get_next_token(tokens)
    if not isinstance(lparen, Paren.LParen):
        raise ParserException(Paren.LParen, lparen)

    #TODO params
    params = []

    rparen = FP.FirstParser.get_next_token(tokens)
    if not isinstance(rparen, Paren.RParen):
        raise ParserException(Paren.RParen, rparen)
    return params


def parseStatements(tokens):
    statements = []
    current = FP.FirstParser.get_next_token(tokens)
    if isinstance(current, Return):
        statements.append(parseReturn(tokens))

    return statements

def parseReturn(tokens):
    return_statement =  ReturnObject(parseConstant(tokens))
    next_token = FP.FirstParser.get_next_token(tokens)
    if not isinstance(next_token, Semicolon):
        raise ParserException(Semicolon, next_token)
    return return_statement

def parseConstant(tokens):
    constant = FP.FirstParser.get_next_token(tokens)
    if not isinstance(constant, Constant):
        raise ParserException(Constant, constant)
    return ConstantObject(constant)




