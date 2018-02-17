from collections import namedtuple

Operator = namedtuple("Operator", "name func priority left_associative")
Number = namedtuple("Number", "value")
Function = namedtuple("Function", "name func priority")

