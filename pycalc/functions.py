from entities import Function, Constant
import math
import types


def math_constants():
    CONSTANTS = {}
    for func in dir(math):
        if isinstance(getattr(math, func), float):
            CONSTANTS[func] = Constant((getattr(math, func)))
    return CONSTANTS


def math_functions():
    FUNCTIONS = {}
    for func in dir(math):
        if callable(getattr(math, func)):
            FUNCTIONS[func] = Function(func, (getattr(math, func)), 15)

    return FUNCTIONS

def builtin_functions():
    glob = globals()
    builtins_dict = glob["__builtins__"]
    BUILTIN_FUNCTIONS = {}
    for func_name, func in builtins_dict.items():
        if isinstance(func, types.BuiltinFunctionType):
            BUILTIN_FUNCTIONS[func_name] = Function(func_name, func, 15)

    return BUILTIN_FUNCTIONS


# print(builtin_functions())

