from entities import Number, Operator
from postfix_notation import generate_postfix_notation
from inspect import getargspec





def execute_operation(operator, numberStack):
    argspec = getargspec(operator)
    operands = []
    for item in range(len(argspec.args)):
        operands.insert(0, numberStack.pop())
        print(numberStack)
    numberStack.append(operator(*operands))
    return numberStack[-1]
    print(numberStack[-1])


def calculate(expression):
    numberStack = []
    for item in generate_postfix_notation(expression):
        if type(item) is Number:
            numberStack.append(item.value)
            print(numberStack)
        elif type(item) is Operator:
            execute_operation(item.func, numberStack)
            print(numberStack)
        else:
            raise ValueError("Unknown type is required.")
    return numberStack[0]
