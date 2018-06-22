from unittest import TestCase
from pycalc import functions
from pycalc.entities import Function, Constant


class TestFunctions(TestCase):

    def test_module_constants(self):
        constants_dict = functions.all_modules_constants(['math', ])
        for i in constants_dict:
            self.assertIsInstance(constants_dict[i], Constant)

    def test_module_functions(self):
        functions_dict = functions.all_modules_functions(['math', ])
        for i in functions_dict:
            self.assertIsInstance(functions_dict[i], Function)

