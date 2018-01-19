from entities import Number, Operator
from postfix_notation import generate_postfix_notation
from inspect import getargspec


def execute_operation(numberStack, Operator):
    argspec = getargspec(Operator)
    operands = []
    for item in range(len(argspec.args)):
        operands.insert(0, numberStack.pop())
    numberberStack.append(Operator(*operands))
    return numberStack[-1]


def calculate(expression):
    numberStack = []
    for item in generate_postfix_notation(expression):
        if type(item) is Number:
            numberStack.append(item.value)
        elif type(item) is Operator:
            execute_operation(item.func, numberStack)
        else:
            raise ValueError("Unknown type is required.")
    return numberStack[0]
