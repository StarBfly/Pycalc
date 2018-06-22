from unittest import TestCase
from pycalc.postfix_notation_generator import PostfixNotation
from entities import Number, Operator, Constant


class TestPostfixNotation(TestCase):

    def test_tokens_check(self):
        expression = "+"
        modules = ['math', ]
        PostfixNotation(expression, modules)
        self.assertRaises(ValueError)

    def test_generate_postfix_notation(self):
        expression = "(2.0**(pi/pi+e/e+2.0**0.0))"
        modules = ['math', ]
        postfix_notation = [Number(value=2.0), Constant(value=3.141592653589793), Constant(value=3.141592653589793),
                            Operator('/', lambda x, y: x / y, 15, True), Constant(value=2.718281828459045),
                            Constant(value=2.718281828459045), Operator('/', lambda x, y: x / y, 15, True),
                            Operator('+ ', lambda x, y: x + y, 10, True), Number(value=2.0), Number(value=0.0),
                            Operator('**', lambda x, y: x ** y, 20, False), Operator('+ ', lambda x, y: x + y, 10, True),
                            Operator('**', lambda x, y: x ** y, 20, False)]
        pn = PostfixNotation(expression, modules)
        for item1, item2 in zip(pn.generate_postfix_notation(), postfix_notation):
            self.assertEqual(type(item1), type(item2))

    def test_generate_post_not_error(self):
        expression = '678*(3+2-1))'
        modules = ['math', ]
        PostfixNotation(expression, modules)
        self.assertRaises(ValueError)
