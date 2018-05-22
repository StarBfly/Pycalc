from entities import Function, Constant
import math
from pprint import pprint as pp

def math_constants():
    CONSTANTS = {}
    for func in dir(math):
        if isinstance(getattr(math, func), float):
            CONSTANTS[func] = Constant((getattr(math, func)))
    return CONSTANTS

#pp(math_constants())


def math_functions():
    FUNCTIONS = {}
    for func in dir(math):
        if callable(getattr(math, func)):
            FUNCTIONS[func] = Function(func, (getattr(math, func)), 0)

    return FUNCTIONS


#print('pi' in math_constants())

#pp(math_functions())