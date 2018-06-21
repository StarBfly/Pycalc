from entities import Operator


def comma(x, y):
    if type(x) is list:
        x.append(y)
        return x
    return [x, y]


OPERATORS = {
    '+ ': Operator('+ ', lambda x, y: x + y, 10, True),
    '- ': Operator('- ', lambda x, y: x - y, 10, True),
    '*': Operator('*', lambda x, y: x * y, 15, True),
    '/': Operator('/', lambda x, y: x / y, 15, True),
    '//': Operator('//', lambda x, y: x // y, 15, True),
    '%': Operator('%', lambda x, y: x % y, 15, True),
    '^': Operator('^', lambda x, y: x ** y, 20, False),
    '**': Operator('**', lambda x, y: x ** y, 20, False),
    ')': Operator(')', None, -1, True),
    '(': Operator('(', None, -1, True),
    '<': Operator('<', lambda x, y: x < y, 2, True),
    '>': Operator('>', lambda x, y: x > y, 2, True),
    '<=': Operator('<=', lambda x, y: x <= y, 2, True),
    '>=': Operator('>=', lambda x, y: x >= y, 2, True),
    '==': Operator('==', lambda x, y: x == y, 2, True),
    '!=': Operator('!=', lambda x, y: x != y, 2, True),
    '-': Operator('-', lambda x: -x, 20, False),
    '+': Operator('+', lambda x: x, 20, False),
    ',': Operator(',', comma, 1, True),

}

COMPARISON_OPERATORS = ['<', '>', '<=', '>=', '==', '!=', '=']
