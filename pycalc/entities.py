from collections import namedtuple


Operator = namedtuple("Operator", "name func priority left_associative")
Number = namedtuple("Number", "value")
Function = namedtuple("Function", "name func priority")

OPERATORS = {
    '+ ': Operator('+ ', lambda x, y: x + y, 10, True),
    '- ': Operator('- ', lambda x, y: x - y, 10, True),
    '*': Operator('*', lambda x, y: x * y, 15, True),
    '/': Operator('/', lambda x, y: x / y, 15, True),
    '//': Operator('//', lambda x, y: x // y, 15, True),
    '%': Operator('%', lambda x, y: x % y, 15, True),
    '^': Operator('^', lambda x, y: x ** y, 20, False),
    ')': Operator(')', None, 5, True),
    '(': Operator('(', None, 5, True),
    '<': Operator('<', lambda x, y: x < y, 0, True),
    '>': Operator('>', lambda x, y: x > y, 0, True),
    '<=': Operator('<=', lambda x, y: x <= y, 0, True),
    '>=': Operator('>=', lambda x, y: x >= y, 0, True),
    '==': Operator('==', lambda x, y: x == y, 0, True), 
    '!=': Operator('!=', lambda x, y: x != y, 0, True),
    '-': Operator('-', lambda x: -x, 20, False),
    '+': Operator('+', lambda x: x, 20, False)
}
