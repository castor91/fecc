#!/usr/bin/env python

from src.fecc_lexer.EasyLexer import EasyLexer
from src.fecc_parser.FirstParser import FirstParser
from src.fecc_code_generator.FirstCodeGenerator import FirstCodeGenerator
from src.fecc_code_optimization.DumbCodeOptimization import DumbCodeOptimization

from os import system, path
import argparse


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Fast Easy C Compiler [fecc]')
    arg_parser.add_argument('input_file', help='Input file')
    arg_parser.add_argument('-o', '--output_file', help='Output file', default=False)
    arg_parser.add_argument('-v', '--verbose', help='[I think is PRINT]', default=False)

    args = arg_parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file if args.output_file else 'a.out'

    with open('{}'.format(input_file), 'r') as infile, open('{}.s'.format(output_file), 'w') as outfile:
        input_string = ''.join(infile.readlines())

        #Lexer
        lexer = EasyLexer(input_string)
        tokens = lexer.lex()

        if args.verbose:
            for t in tokens:
                print t,
            print
        #Parser
        parser = FirstParser()
        codes = parser.parseProgram(tokens)
        if args.verbose:
            for c in codes:
                print c

        #Parser Optimization
        optimization = DumbCodeOptimization()
        optimized_code = optimization.optimize_parsing(codes)

        #Code Generation
        out_code = []
        generator = FirstCodeGenerator.generate(optimized_code, out_code)

        #Code Optimization
        optimized_code = optimization.optimize_code(out_code)

        #File Creation
        for instruction in optimized_code:
            print instruction.generate()
            outfile.write('{}\n'.format(instruction.generate()))

    print '[+] Linking and Assemble on output file: {}'.format(output_file)
    system('gcc -m32 {0}.s -o {0}'.format(output_file))
    system('rm {}.s'.format(output_file))
