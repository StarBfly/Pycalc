from pycalc.entities import Function, Constant
import importlib
import types


def upload_module_constants(module):
    """Uploads all constants from given module into dictionary of Constant-objects"""
    constants = {}
    for func in dir(module):
        if isinstance(getattr(module, func), float):
            constants[func] = Constant((getattr(module, func)))

    return constants


def upload_module_functions(module):
    """Uploads all functions from given module into dictionary of Function-objects"""
    functions = {}
    for func in dir(module):
        if callable(getattr(module, func)):
            functions[func] = Function(func, (getattr(module, func)), 15)

    return functions


def all_modules_constants(modules_list):
    """Uploads all constants from given list of modules"""
    constants_dict = {}
    for module in modules_list:
        module = importlib.__import__(module)
        constants_dict.update(upload_module_constants(module))
    return constants_dict


def all_modules_functions(modules_list):
    """Uploads all functions from given list of modules"""
    funcs_dict = {}
    for module in modules_list:
        module = importlib.__import__(module)
        funcs_dict.update(upload_module_functions(module))
    return funcs_dict


def builtin_functions():
    """ Adds all builtin-functions into dictionary of Function-objects """
    glob = globals()
    builtins_dict = glob["__builtins__"]
    builtin_funcs = {}
    for func_name, func in builtins_dict.items():
        if isinstance(func, types.BuiltinFunctionType):
            builtin_funcs[func_name] = Function(func_name, func, 15)

    return builtin_funcs
