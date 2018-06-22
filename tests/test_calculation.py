from unittest import TestCase
from pycalc import calculation
from unittest.mock import patch
from pycalc.postfix_notation_generator import PostfixNotation
import math
from pycalc.entities import Number, Constant, Function, Operator


class TestCalculation(TestCase):

    def test_calculate(self):
        expression = "(2.0**(pi/pi+e/e+2.0**0.0))"
        modules = ['math', ]
        postfix_notation = [Number(value=2.0), Constant(value=3.141592653589793), Constant(value=3.141592653589793),
                            Operator('/', lambda x, y: x / y, 15, True), Constant(value=2.718281828459045),
                            Constant(value=2.718281828459045), Operator('/', lambda x, y: x / y, 15, True),
                            Operator('+ ', lambda x, y: x + y, 10, True), Number(value=2.0), Number(value=0.0),
                            Operator('**', lambda x, y: x ** y, 20, False),
                            Operator('+ ', lambda x, y: x + y, 10, True), Operator('**', lambda x, y: x ** y, 20, False)]
        with patch.object(PostfixNotation, 'generate_postfix_notation', return_value=postfix_notation) as mock_method:
            post_not = PostfixNotation(expression, modules)
            post_not.generate_postfix_notation()
        mock_method.assert_called_once_with()
        self.assertEqual((2.0**(math.pi/math.pi+math.e/math.e+2.0**0.0)), calculation.calculate(expression))

    def test_calculate_exception(self):
        expression = "ee"
        modules = ['math', ]
        postfix_notation = [Constant(value=2.718281828459045), Constant(value=2.718281828459045)]
        with patch.object(PostfixNotation, 'generate_postfix_notation', return_value=postfix_notation) as mock_method:
            post_not = PostfixNotation(expression, modules)
            post_not.generate_postfix_notation()
        mock_method.assert_called_once_with()
        self.assertRaises(ValueError)

    def test_calculation_num(self):
        expression = "123456778"
        modules = ['math', ]
        postfix_notation = [Number(value=123456778.0)]
        with patch.object(PostfixNotation, 'generate_postfix_notation', return_value=postfix_notation) as mock_method:
            post_not = PostfixNotation(expression, modules)
            post_not.generate_postfix_notation()
        mock_method.assert_called_once_with()
        self.assertEqual(123456778, calculation.calculate(expression))

    def test_calculation_func_consts(self):
        expression = "log(e)"
        modules = ['math', ]
        postfix_notation = [Constant(value=2.718281828459045), Function(name='log', func='log', priority=15)]
        with patch.object(PostfixNotation, 'generate_postfix_notation', return_value=postfix_notation) as mock_method:
            post_not = PostfixNotation(expression, modules)
            post_not.generate_postfix_notation()
        mock_method.assert_called_once_with()
        self.assertEqual(math.log(math.e), calculation.calculate(expression))

