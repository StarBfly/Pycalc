from entities import *
from functions import all_modules_constants, all_modules_functions, builtin_functions
from operators import OPERATORS, COMPARISSON_OPERATORS


class Parser(object):
    _functions = all_modules_functions()
    _constants = all_modules_constants()
    _built_in_functions = builtin_functions()
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
    def _is_builtin(cls, substring):
        return substring in cls._built_in_functions

    @classmethod
    def _is_constant(cls, substring):
        return substring in cls._constants

    @classmethod
    def _replace_sign(cls, expression):
        expression = expression.replace("+", "+ ")
        expression = expression.replace("-", "- ")
        return expression

    @classmethod
    def _remove_spaces(cls, expression):
        for index, item in enumerate(expression):
            if cls._is_number(item) or cls._is_constant(item):
                if index + 2 >= len(expression):
                    continue
                next_to_space_item = expression[index + 2]
                if expression[index + 1] == " " and (cls._is_number(next_to_space_item) or cls._is_constant(next_to_space_item)):
                    raise ValueError("ERROR: to many unnecessary spaces.")
            elif cls._is_operator(item):
                if item == "*" or item == "/":
                    if index + 2 >= len(expression):
                        continue
                    next_to_space_item = expression[index + 2]
                    if expression[index + 1] == " " and expression[next_to_space_item] == item:
                        raise ValueError("ERROR: to many unnecessary spaces.")
                elif item in COMPARISSON_OPERATORS:
                    if index + 2 >= len(expression):
                        continue
                    next_to_space_item = expression[index + 2]
                    if expression[index + 1] == " " and expression[next_to_space_item] in COMPARISSON_OPERATORS:
                        raise ValueError("ERROR: to many unnecessary spaces.")

            elif item == " " or cls._is_function(item) or cls._is_builtin(item):
                continue
            else:
                expression = expression.replace(" ", "")
        expression = expression.expandtabs(0)
        return expression

    @classmethod
    def _change_signs(cls, parsed_exp):
        is_changed = False
        for idx in range(len(parsed_exp)-1):
            if type(parsed_exp[idx]) is Operator and parsed_exp[idx].name in ("- ", "+ "):
                if isinstance(parsed_exp[idx +1], Number) or (isinstance(parsed_exp[idx+1], Operator) and parsed_exp[idx+1].name in ["(", "-", "+"]) or isinstance(parsed_exp[idx+1], Function) or isinstance(parsed_exp[idx+1], Constant):
                    if idx == 0:
                        parsed_exp[idx] = OPERATORS[parsed_exp[idx].name.strip()]
                        is_changed = True
                    elif isinstance(parsed_exp[idx - 1], Operator) and parsed_exp[idx-1].name != ")":
                        parsed_exp[idx] = OPERATORS[parsed_exp[idx].name.strip()]
                        is_changed = True
        return is_changed, parsed_exp

    @classmethod
    def tokens_check(cls, expression, parsed_expression):
        nums_constants_list = []
        for token in parsed_expression:
            if isinstance(token, Number) or isinstance(token, Constant):
                nums_constants_list.append(token)
        if len(nums_constants_list) == 0:
            raise ValueError(f'Sorry, but "{expression}" is not enough for me to calculate.'
                             "ERROR: missing numbers or constants")

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
                if end_index != len(expression):
                    if expression[end_index] == '(':
                        parsed_exp.append(OPERATORS['*'])
                start_index = end_index
                end_index = len(expression)
            elif cls._is_operator(substring):
                parsed_exp.append(OPERATORS[substring])
                if substring == ')':
                    if expression.index(substring) != len(expression)-1:
                        if cls._is_number(expression[expression.index(substring) + 1]) \
                                or expression[expression.index(substring) + 1] == '(':
                            parsed_exp.append(OPERATORS['*'])
                start_index = end_index
                end_index = len(expression)
            elif cls._is_builtin(substring):
                parsed_exp.append(cls._built_in_functions[substring])
                start_index = end_index
                end_index = len(expression)
            elif cls._is_function(substring):
                parsed_exp.append(cls._functions[substring])
                start_index = end_index
                end_index = len(expression)
            elif cls._is_constant(substring):
                parsed_exp.append(cls._constants[substring])
                start_index = end_index
                end_index = len(expression)
            else:
                end_index -= 1
                if end_index == start_index:
                    raise ValueError(f'"{substring}" can not be parsed.')
        is_changed, parsed_exp = cls._change_signs(parsed_exp)
        while is_changed:
            is_changed, parsed_exp = cls._change_signs(parsed_exp)
        return parsed_exp

    @classmethod
    def generate_postfix_notation(cls, expression):
        parsed_expression = cls.parse_expression(expression)
        cls.tokens_check(expression, parsed_expression)
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
            elif isinstance(token, Constant):
                postfix_notation.append(token)
            else:
                raise ValueError(f' "{token}" :unknown object')
        while operators_stack:
            if isinstance(operators_stack[-1], Number):
                raise ValueError('Parenthesis are not balanced.')
            postfix_notation.append(operators_stack.pop())

        return postfix_notation
