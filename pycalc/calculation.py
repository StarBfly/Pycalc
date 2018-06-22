from pycalc.entities import is_operator, is_num, is_const, is_func
from pycalc import postfix_notation_generator
from inspect import getfullargspec
from pycalc.error_codes import TYPE_ERROR, MALFORMED_EXPRESSION


def _execute_operation(operator, number_stack):
    argspec = getfullargspec(operator)
    operands = []
    for item in range(len(argspec.args)):
        operands.insert(0, number_stack.pop())
    number_stack.append(operator(*operands))
    return number_stack[-1]


def _execute_function(func, number_stack):
    x = number_stack.pop()
    if type(x) is list:
        number_stack.append(func(*x))
    else:
        number_stack.append(func(x))


def calculate(expression, modules=None):
    """Calculate given expression
    :param expression:
    :param modules: list of uploaded modules"""
    number_stack = []
    modules = ["math", ] if not modules else ["math", ] + modules
    postfix = postfix_notation_generator.PostfixNotation(expression, modules)
    for item in postfix.generate_postfix_notation():
        if is_num(item):
            number_stack.append(item.value)
        elif is_const(item):
            number_stack.append(item.value)
        elif is_operator(item):
            _execute_operation(item.func, number_stack)
        elif is_func(item):
            _execute_function(item.func, number_stack)
        else:
            raise TypeError(TYPE_ERROR)
    if len(number_stack) > 1:
        raise ValueError(MALFORMED_EXPRESSION)
    return number_stack[0]
