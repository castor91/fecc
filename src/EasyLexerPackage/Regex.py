import re
import EasyLexerPackage.MatchFunction as MF

string_regex = r'^(\s*)([a-zA-Z][a-zA-Z0-9_]*)'
number_regex = r'^(\s*)([1-9][0-9]*|0x[a-fA-F0-9]*|0[1-7]*)' #Match base 10, 16 and 8
paren_regex = r'^(\s*)(\(|\)|\[|\]|{|})'
semicolon_regex = r'^(\s*)(;)'
eof_regex = r'^(\s*)()$' #Second grups for correct match

string_regex_compiled = re.compile(string_regex)
number_regex_compiled = re.compile(number_regex)
paren_regex_compiled = re.compile(paren_regex)
semicolon_regex_compiled = re.compile(semicolon_regex)
eof_regex_compiled = re.compile(eof_regex)

regexs = {string_regex_compiled: MF.string_match,
          number_regex_compiled: MF.number_match,
          paren_regex_compiled: MF.paren_match,
          semicolon_regex_compiled: MF.semicolon_match,
          eof_regex_compiled: MF.eof_match,
}