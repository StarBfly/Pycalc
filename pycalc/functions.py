from pycalc.entities import Function, Constant
from launcher import _parse_args
import importlib
import types


def upload_module_constants(module):
    constants = {}
    for func in dir(module):
        if isinstance(getattr(module, func), float):
            constants[func] = Constant((getattr(module, func)))

    return constants


def upload_module_functions(module):
    functions = {}
    for func in dir(module):
        if callable(getattr(module, func)):
            functions[func] = Function(func, (getattr(module, func)), 15)

    return functions


def all_modules_constants():
    args = _parse_args()
    module_list = ["math", ] + args.m
    constants_dict = {}
    for module in module_list:
        module = importlib.__import__(module)
        constants_dict.update(upload_module_constants(module))
    return constants_dict


def all_modules_functions():
    args = _parse_args()
    module_list = ["math", ] + args.m
    funcs_dict = {}
    for module in module_list:
        module = importlib.__import__(module)
        funcs_dict.update(upload_module_constants(module))
    return funcs_dict


def builtin_functions():
    glob = globals()
    builtins_dict = glob["__builtins__"]
    builtin_funcs = {}
    for func_name, func in builtins_dict.items():
        if isinstance(func, types.BuiltinFunctionType):
            builtin_funcs[func_name] = Function(func_name, func, 15)

    return builtin_funcs
