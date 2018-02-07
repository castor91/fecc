import re
import MatchFunction as MF

#Stage 1
string_regex = r'^(\s*)([a-zA-Z][a-zA-Z0-9_]*)'
number_regex = r'^(\s*)([1-9][0-9]*|0x[a-fA-F0-9]*|0[1-7]*)' #Match base 10, 16 and 8
paren_regex = r'^(\s*)(\(|\)|\[|\]|{|})'
semicolon_regex = r'^(\s*)(;)'
eof_regex = r'^(\s*)()$' #Second grups for correct match

#Stage 2
negation_regex = r'^(\s*)(\-)'
bitwise_regex = r'^(\s*)(~)'
logical_negation_regex = r'^(\s*)(\!)'

#Stage 3
addition_regex = r'^(\s*)(\+)'
multiplication_regex = r'(\s*)(\*)'
division_regex = r'(\s*)(/)'

#Stage 4
logical_and_regex = r'^(\s*)(&&)'
logical_or_regex = r'^(\s*)(\|\|)'
eq_regex = r'^(\s*)(==)'
neq_regex = r'^(\s*)(\!=)'
lte_regex = r'^(\s*)(<=)'
lt_regex = r'^(\s*)(<)'
gte_regex = r'^(\s*)(>=)'
gt_regez = r'^(\s*)(>)'


#Stage 1
string_regex_compiled = re.compile(string_regex)
number_regex_compiled = re.compile(number_regex)
paren_regex_compiled = re.compile(paren_regex)
semicolon_regex_compiled = re.compile(semicolon_regex)
eof_regex_compiled = re.compile(eof_regex)

#Stage 2
negation_regex_compiled = re.compile(negation_regex)
bitwise_regex_compiled = re.compile(bitwise_regex)
logical_negation_regex_compiled = re.compile(logical_negation_regex)

#Stage 3
addition_regex_compiled = re.compile(addition_regex)
multiplication_regex_compiled = re.compile(multiplication_regex)
division_regex_compiled = re.compile(division_regex)

#Stage 4
logical_and_regex_compiled = re.compile(logical_and_regex)
logical_or_regex_compiled = re.compile(logical_or_regex)
eq_regex_compiled = re.compile(eq_regex)
neq_regex_compiled = re.compile(neq_regex)
lte_regex_compiled = re.compile(lte_regex)
lt_regex_compiled = re.compile(lt_regex)
gte_regex_compiled = re.compile(gte_regex)
gt_regex_compiled = re.compile(gt_regez)

#Final
regexs = {string_regex_compiled: MF.string_match,
          number_regex_compiled: MF.number_match,
          paren_regex_compiled: MF.paren_match,
          semicolon_regex_compiled: MF.semicolon_match,
          eof_regex_compiled: MF.eof_match,

          negation_regex_compiled: MF.negation_match,
          bitwise_regex_compiled: MF.bitwise_match,
          logical_negation_regex_compiled: MF.logical_negation_match,

          addition_regex_compiled: MF.addition_match,
          multiplication_regex_compiled: MF.multiplication_match,
          division_regex_compiled: MF.division_match,

          logical_and_regex_compiled: MF.logical_and_match,
          logical_or_regex_compiled: MF.logical_or_match,
          eq_regex_compiled: MF.eq_match,
          neq_regex_compiled: MF.neq_match,
          lte_regex_compiled: MF.lte_match,
          lt_regex_compiled: MF.lt_match,
          gte_regex_compiled: MF.gte_match,
          gt_regex_compiled: MF.gt_match,
}