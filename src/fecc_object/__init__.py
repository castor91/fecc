import os

module_name = os.path.dirname(os.path.relpath(__file__))
names = filter(lambda x: not x.endswith('.pyc'), [name for name in os.listdir(module_name) if name not in ['__init__.py']])

for name in names:
    globals()[name[:-3]] = getattr(__import__(name[:-3], globals(), locals(), [name], -1), name[:-3])
