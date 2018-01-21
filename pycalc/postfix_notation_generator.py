from entities import Operator, Number


def generate_postfix_notation(parsed_expression):
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
                    raise ValueError('Parenthesis are not balanced.m')
            else:
                if not token.left_associative:
                    while operators_stack and token.priority < operators_stack[-1].priority:
                        postfix_notation.append(operators_stack.pop())
                else:
                    while operators_stack and token.priority <= operators_stack[-1].priority:
                        postfix_notation.append(operators_stack.pop())
                operators_stack.append(token)
        else:
            raise ValueError(f' "{token}" :unknown object')
    while operators_stack:
        if not isinstance(operators_stack[-1], Operator):
            raise ValueError('Parenthesis are not balanced.')
        postfix_notation.append(operators_stack.pop())

    return postfix_notation




