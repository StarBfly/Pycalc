from collections import namedtuple


Operator = namedtuple("Operator", "name func priority left_associative")
Number = namedtuple("Number", "value")

OPERATORS = {
    '+ ': Operator('+ ', lambda x, y: x + y, 5, True),
    '- ': Operator('- ', lambda x, y: x - y, 5, True),
    '*': Operator('*', lambda x, y: x * y, 10, True),
    '/': Operator('/', lambda x, y: x / y, 10, True),
    '//': Operator('//', lambda x, y: x // y, 10, True),
    '%': Operator('%', lambda x, y: x % y, 10, True),
    '^': Operator('^', lambda x, y: x ** y, 20, False),
    ')': Operator(')', None, 0, True),
    '(': Operator('(', None, 0, True)
}
