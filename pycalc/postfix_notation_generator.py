from entities import Number, Operator, Function, Constant
from pyparser import Parser
from error_codes import NUMS_CONST_MISSING, WRONG_PLACED_PARENTHESIS, unknown_object


class PostfixNotation:
    def __init__(self, expression):
        self.parser = Parser(expression)
        self.parsed_expression = self.parser.parse_expression()

    def tokens_check(self):
        nums_constants_list = []
        for token in self.parsed_expression:
            if isinstance(token, Number) or isinstance(token, Constant):
                nums_constants_list.append(token)
        if len(nums_constants_list) == 0:
            raise ValueError(NUMS_CONST_MISSING)

    def generate_postfix_notation(self):
        self.tokens_check()
        postfix_notation = []
        operators_stack = []
        for token in self.parsed_expression:
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
                        raise ValueError(WRONG_PLACED_PARENTHESIS)
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
                raise TypeError(unknown_object(token))
        while operators_stack:
            if isinstance(operators_stack[-1], Number):
                raise ValueError(WRONG_PLACED_PARENTHESIS)
            postfix_notation.append(operators_stack.pop())

        return postfix_notation
