import os


module_name = os.path.dirname(os.path.relpath(__file__))
names = filter(lambda x: not x.endswith('.pyc'), [name for name in os.listdir(module_name) if name not in ['__init__.py']])

for name in names:
    globals()[name[:-3]] = getattr(__import__(name[:-3], globals(), locals(), [name], -1), name[:-3])

# TODO refactoring for dynamic include all parens
from Paren import LParen as LParen
from Paren import RParen as RParen
from Paren import LBrace as LBrace
from Paren import RBrace as RBrace


