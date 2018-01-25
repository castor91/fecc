import EasyLexer

if __name__ == '__main__':
    print 'Fast Easy C Compiler [fecc]'
    with open('input.c', 'r') as infile, open('../bin/out.s', 'w') as outfile:
        input_string = ''.join(infile.readlines())
        lex = EasyLexer.EasyLexer(input_string)
        tokens = lex.lex()
        for i in tokens:
            print i,