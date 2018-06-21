from entities import is_const, is_num, is_operator, is_func, Number
from functions import all_modules_constants, all_modules_functions, builtin_functions
from operators import OPERATORS, COMPARISON_OPERATORS
from error_codes import EXTRA_SPACES, nonparsable_substring


class Parser(object):
    _functions = all_modules_functions()
    _constants = all_modules_constants()
    _built_in_functions = builtin_functions()
    _operators = OPERATORS
    _number = Number

    def __init__(self, expression):
        self.expression = expression

    @staticmethod
    def _is_number(substring):
        try:
            float(substring)
        except ValueError:
            return False
        return True

    @staticmethod
    def _is_operator(substring):
        return substring in Parser._operators

    @staticmethod
    def _is_function(substring):
        return substring in Parser._functions

    @staticmethod
    def _is_builtin(substring):
        return substring in Parser._built_in_functions

    @staticmethod
    def _is_constant(substring):
        return substring in Parser._constants

    @staticmethod
    def _replace_sign(expression):
        expression = expression.replace("+", "+ ")
        expression = expression.replace("-", "- ")
        return expression

    @staticmethod
    def _update_substring(expression, end_index):
        start_index = end_index
        end_index = len(expression)
        return start_index, end_index

    def _next_item_is_space(self, index):
        next_item = self.expression[index + 1]
        return next_item == " "

    @staticmethod
    def _add_implicit_multiplication(expression, substring, end_index, parsed_exp):
        if Parser._is_number(substring):
            if end_index != len(expression):
                next_item = expression[end_index]
                if next_item == '(':
                    parsed_exp.append(OPERATORS['*'])
        elif substring == ')':
            if expression.index(substring) != len(expression) - 1:
                next_item_index = expression.index(substring) + 1
                next_item = expression[next_item_index]
                if Parser._is_number(next_item) or next_item == '(':
                    parsed_exp.append(OPERATORS['*'])

    def _last_item_is_space(self, index):
        return index + 2 >= len(self.expression)

    def _check_spaces_nums_const(self, index):
        if not self._last_item_is_space(index):
            next_to_space_item = self.expression[index + 2]
            after_space_is_num = Parser._is_number(next_to_space_item)
            after_space_is_const = Parser._is_constant(next_to_space_item)
            if self._next_item_is_space(index) and (after_space_is_num or after_space_is_const):
                raise ValueError(EXTRA_SPACES)

    def _check_spaces_operator(self, index, item):
        if item == "*" or item == "/":
            if not self._last_item_is_space(index):
                next_to_space_item = self.expression[index + 2]
                if self._next_item_is_space(index) and next_to_space_item == item:
                    raise ValueError(EXTRA_SPACES)

        elif item in COMPARISON_OPERATORS:
            if not self._last_item_is_space(index):
                next_to_space_item = self.expression[index + 2]
                if self._next_item_is_space(index) and next_to_space_item in COMPARISON_OPERATORS:
                    raise ValueError(EXTRA_SPACES)

    def _remove_spaces(self):
        for index, item in enumerate(self.expression):
            if Parser._is_number(item) or Parser._is_constant(item):
                self._check_spaces_nums_const(index)
            elif Parser._is_operator(item):
                self._check_spaces_operator(index, item)

        expression = self.expression.replace(" ", "")
        expression = expression.expandtabs(0)

        return expression

    @staticmethod
    def add_unary_minus(parsed_exp, index, item):
        previous_item = parsed_exp[index - 1]
        if index == 0 or (is_operator(previous_item) and previous_item.name != ")"):
            parsed_exp[index] = OPERATORS[item.name.strip()]
            is_changed = True
        else:
            is_changed = False
        return is_changed, parsed_exp

    @staticmethod
    def change_signs(parsed_exp):
        is_changed = False
        for index in range(len(parsed_exp)-1):
            item = parsed_exp[index]
            next_item = parsed_exp[index+1]
            if is_operator(item) and item.name in ("- ", "+ "):
                if is_num(next_item):
                    is_changed, parsed_exp = Parser.add_unary_minus(parsed_exp, index, item)
                elif is_operator(next_item) and next_item.name in ["(", "-", "+"]:
                    is_changed, parsed_exp = Parser.add_unary_minus(parsed_exp, index, item)
                elif is_num(next_item) or is_const(next_item):
                    is_changed, parsed_exp = Parser.add_unary_minus(parsed_exp, index, item)
                elif is_func(next_item):
                    is_changed, parsed_exp = Parser.add_unary_minus(parsed_exp, index, item)

        return is_changed, parsed_exp

    def parse_expression(self):
        expression = self._remove_spaces()
        expression = Parser._replace_sign(expression)
        start_index = 0
        end_index = len(expression)
        parsed_exp = []
        while start_index != len(expression):
            substring = expression[start_index:end_index]
            if Parser._is_number(substring):
                parsed_exp.append(Number(float(substring)))
                Parser._add_implicit_multiplication(expression, substring, end_index, parsed_exp)
                start_index, end_index = Parser._update_substring(expression, end_index)
            elif Parser._is_operator(substring):
                parsed_exp.append(OPERATORS[substring])
                Parser._add_implicit_multiplication(expression, substring, end_index, parsed_exp)
                start_index, end_index = Parser._update_substring(expression, end_index)
            elif Parser._is_builtin(substring):
                parsed_exp.append(Parser._built_in_functions[substring])
                start_index, end_index = Parser._update_substring(expression, end_index)
            elif Parser._is_function(substring):
                parsed_exp.append(Parser._functions[substring])
                start_index, end_index = Parser._update_substring(expression, end_index)
            elif Parser._is_constant(substring):
                parsed_exp.append(Parser._constants[substring])
                start_index, end_index = Parser._update_substring(expression, end_index)
            else:
                end_index -= 1
                if end_index == start_index:
                    raise ValueError(nonparsable_substring(substring))
        is_changed, parsed_exp = Parser.change_signs(parsed_exp)
        while is_changed:
            is_changed, parsed_exp = Parser.change_signs(parsed_exp)
        return parsed_exp
