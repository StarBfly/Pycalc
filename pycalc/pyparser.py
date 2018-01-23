from entities import OPERATORS, Number, Operator


def parse_expression(expression):
    expression = expression.replace(" ", "")
    expression = expression.expandtabs(0)
    expression = expression.replace("+", "+ ")
    expression = expression.replace("-", "- ")
    start_index = 0
    end_index = len(expression)
    parsed_exp = []
    while start_index != len(expression):
        substring_to_check = expression[start_index:end_index]
        if is_number(substring_to_check):
            parsed_exp.append(Number(float(substring_to_check)))
            start_index = end_index
            end_index = len(expression)
        elif is_operator(substring_to_check):
            parsed_exp.append(OPERATORS[substring_to_check])
            start_index = end_index
            end_index = len(expression)
        else:
            end_index -= 1
            if end_index == start_index:
                raise ValueError(f'"{substring_to_check}" can not be parsed.')
    x = 0
    while x < len(parsed_exp):
        if type(parsed_exp[x]) is Operator and parsed_exp[x].name in ("- ", "+ "):
                if x == 0 or type(parsed_exp[x-1]) is Operator:
                    parsed_exp[x] = OPERATORS[parsed_exp[x].name.strip()]
        x += 1

    return parsed_exp


def is_number(substring):
    try:
        float(substring)
    except ValueError:
        return False
    return True


def is_operator(substring):
    return substring in OPERATORS

    
def is_function(substring):
    pass
    