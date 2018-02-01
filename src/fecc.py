#!/usr/bin/env python

from fecc_lexer.EasyLexer import EasyLexer
#from first_object.FirstParser import FirstParser
from fecc_parser.FirstParser import FirstParser
from fecc_code_generator.FirstCodeGenerator import FirstCodeGenerator
from fecc_code_optimization.DumbCodeOptimization import DumbCodeOptimization

from sys import argv
from os import system, path

if __name__ == '__main__':
    print 'Fast Easy C Compiler [fecc]'
    input_file = argv[1]
    output_file = '{}'.format(path.splitext(input_file)[0]) if len(argv) == 2 else argv[2]
    with open('{}'.format(input_file), 'r') as infile, open('{}.s'.format(output_file), 'w') as outfile:
        input_string = ''.join(infile.readlines())

        #Lexer
        lexer = EasyLexer(input_string)
        tokens = lexer.lex()

        if '-p' in argv:
            for t in tokens:
                print t

        #Parser
        parser = FirstParser()
        codes = parser.parseProgram(tokens)
        if '-p' in argv:
            for c in codes:
                print c

        #Parser Optimization
        optimization = DumbCodeOptimization()
        optimized_code = optimization.optimize_parsing(codes)

        #Code Generation
        out_code = []
        generator = FirstCodeGenerator.generate(optimized_code, out_code)
        for g in out_code:
            print g
        raw_input()
        #Code Optimization
        optimized_code = optimization.optimize_code(out_code)

        #File Creation
        for instruction in optimized_code:
            outfile.write('{}\n'.format(instruction))

    print '[+] Linking and Assemble on output file: {}'.format(output_file)
    system('gcc -m32 {0}.s -o {0}'.format(output_file))
    system('rm {}.s'.format(output_file))
