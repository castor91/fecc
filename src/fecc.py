#!/usr/bin/env python

from EasyLexerPackage.EasyLexer import EasyLexer
from DumpCodeOptimization import DumpCodeOptimization
from FirstCodeGenerator import FirstCodeGenerator
import FirstParser
from sys import argv
from os import system, path

if __name__ == '__main__':
    print 'Fast Easy C Compiler [fecc]'
    input_file = argv[1]
    output_file = '{}'.format(path.splitext(input_file)[0]) if len(argv) == 2 else argv[2]
    with open('{}'.format(input_file), 'r') as infile, open('{}.s'.format(output_file), 'w') as outfile:
        input_string = ''.join(infile.readlines())
        lexer = EasyLexer(input_string)
        tokens = lexer.lex()

        parser = FirstParser.FirstParser()
        codes = parser.parse(tokens)
        if '-p' in argv:
            for c in codes:
                print c
        else:
            optimization = DumpCodeOptimization()
            optimized_code = optimization.optimize(codes)

            generator = FirstCodeGenerator.generate(optimized_code, outfile)

            print '[+] Linking and Assemble on output file: {}'.format(output_file)
            system('gcc -m32 {0}.s -o {0}'.format(output_file))
            system('rm {}.s'.format(output_file))
