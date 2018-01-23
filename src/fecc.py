import lexer

if __name__ == '__main__':
    print 'Fast Easy C Compiler [fecc]'
    with open('input.c', 'r') as infile, open('../bin/out.s', 'w') as outfile:
        input_string = ''.join(infile.readlines())
        lex = lexer.Lexer(input_string)
        print lex.lex()