from entities import Number, Operator
from postfix_notation_generator import generate_postfix_notation
from inspect import getargspec





def execute_operation(operator, numberStack):
    argspec = getargspec(operator)
    operands = []
    for item in range(len(argspec.args)):
        operands.insert(0, numberStack.pop())
    numberStack.append(operator(*operands))
    return numberStack[-1]


def calculate(postfix_notation):
    numberStack = []
    for item in postfix_notation:
        if type(item) is Number:
            numberStack.append(item.value)
        elif type(item) is Operator:
            execute_operation(item.func, numberStack)
        else:
            raise ValueError("Unknown type is required.")
    return numberStack[0]
