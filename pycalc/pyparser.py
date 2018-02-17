from entities import Number, Operator, Function
from functions import FUNCTIONS
from operators import OPERATORS


class Parser(object):
    _functions = FUNCTIONS
    _operators = OPERATORS
    _number = Number

    @classmethod
    def _is_number(cls, substring):
        try:
            float(substring)
        except ValueError:
            return False
        return True

    @classmethod
    def _is_operator(cls, substring):
        return substring in cls._operators

    @classmethod
    def _is_function(cls, substring):
        return substring in cls._functions

    @classmethod
    def _replace_sign(cls, expression):
        expression = expression.replace("+", "+ ")
        expression = expression.replace("-", "- ")
        return expression

    @classmethod
    def _remove_spaces(cls, expression):
        expression = expression.replace(" ", "")
        expression = expression.expandtabs(0)
        return expression

    @classmethod
    def _change_signs(cls, parsed_exp):
        x = 0
        while x < len(parsed_exp):
            if type(parsed_exp[x]) is Operator and parsed_exp[x].name in ("- ", "+ "):
                if x == 0 or type(parsed_exp[x - 1]) is Operator:
                    if parsed_exp[x - 1].name != ")":
                        parsed_exp[x] = OPERATORS[parsed_exp[x].name.strip()]
            x += 1
        return parsed_exp

    @classmethod
    def parse_expression(cls, expression):
        expression = cls._remove_spaces(expression)
        expression = cls._replace_sign(expression)
        start_index = 0
        end_index = len(expression)
        parsed_exp = []
        while start_index != len(expression):
            substring = expression[start_index:end_index]
            if cls._is_number(substring):
                parsed_exp.append(Number(float(substring)))
                start_index = end_index
                end_index = len(expression)
            elif cls._is_operator(substring):
                parsed_exp.append(OPERATORS[substring])
                start_index = end_index
                end_index = len(expression)
            elif cls._is_function(substring):
                parsed_exp.append(FUNCTIONS[substring])
                start_index = end_index
                end_index = len(expression)
            else:
                end_index -= 1
                if end_index == start_index:
                    raise ValueError(f'"{substring}" can not be parsed.')
        parsed_exp = cls._change_signs(parsed_exp)
        return parsed_exp

    @classmethod
    def generate_postfix_notation(cls, expression):
        parsed_expression = cls.parse_expression(expression)
        postfix_notation = []
        operators_stack = []
        for token in parsed_expression:
            if isinstance(token, Number):
                postfix_notation.append(token)
            elif isinstance(token, Operator):
                if token.name == '(':
                    operators_stack.append(token)
                elif token.name == ')':
                    while operators_stack and operators_stack[-1].name != '(':
                        postfix_notation.append(operators_stack.pop())
                    if operators_stack:
                        operators_stack.pop()
                    else:
                        raise ValueError('Parenthesis are not balanced.')
                else:
                    if not token.left_associative:
                        while operators_stack and token.priority < operators_stack[-1].priority:
                            postfix_notation.append(operators_stack.pop())
                    else:
                        while operators_stack and token.priority <= operators_stack[-1].priority:
                            postfix_notation.append(operators_stack.pop())
                    operators_stack.append(token)
            elif isinstance(token, Function):
                operators_stack.append(token)
            else:
                raise ValueError(f' "{token}" :unknown object')
        while operators_stack:
            if isinstance(operators_stack[-1], Number):
                raise ValueError('Parenthesis are not balanced.')
            postfix_notation.append(operators_stack.pop())

        return postfix_notation
