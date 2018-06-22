from collections import namedtuple

Operator = namedtuple("Operator", "name func priority left_associative")
Number = namedtuple("Number", "value")
Function = namedtuple("Function", "name func priority")
Constant = namedtuple("Constant", "value")


def is_operator(item):
    return isinstance(item, Operator)


def is_num(item):
    return isinstance(item, Number)


def is_func(item):
    return isinstance(item, Function)


def is_const(item):
    return isinstance(item, Constant)
