#!/usr/bin/env python

from EasyLexerPackage.EasyLexer import EasyLexer
from DumpCodeOptimization import DumpCodeOptimization
from FirstCodeGenerator import FirstCodeGenerator
import FirstParser
from sys import argv

if __name__ == '__main__':
    print 'Fast Easy C Compiler [fecc]'
    with open('{}'.format(argv[1]), 'r') as infile, open('{}.my_out'.format('.'.join(argv[1].split('.')[:-1])), 'w') as outfile:
        input_string = ''.join(infile.readlines())
        lexer = EasyLexer(input_string)
        tokens = lexer.lex()

        parser = FirstParser.FirstParser()
        codes = parser.parse(tokens)

        optimization = DumpCodeOptimization()
        optimized_code = optimization.optimize(codes)

        generator = FirstCodeGenerator()
        generator.generate(optimized_code, outfile)
