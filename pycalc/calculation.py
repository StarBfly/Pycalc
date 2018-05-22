from entities import *
from pyparser import Parser
from inspect import getargspec


def _execute_operation(operator, number_stack):
    argspec = getargspec(operator)
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


def calculate(expression):
    number_stack = []
    for item in Parser.generate_postfix_notation(expression):
        if type(item) is Number:
            number_stack.append(item.value)
        elif type(item) is Constant:
            number_stack.append(item.value)
        elif type(item) is Operator:
            _execute_operation(item.func, number_stack)
        elif type(item) is Function:
            _execute_function(item.func, number_stack)
        else:
            raise ValueError("Unknown type is required.")
    if len(number_stack) > 1:
            raise ValueError('Expression malformed')  # ToDo: find the reason of the problem, write the comment more specific.
    return number_stack[0]
