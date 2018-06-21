TYPE_ERROR = "ERROR: Unknown type is required."

MALFORMED_EXPRESSION = "ERROR: Expression is composed incorrectly."

NUMS_CONST_MISSING = "Sorry, but your expression is not enough for me to calculate. " \
                     "ERROR: Missing numbers or constants."

WRONG_PLACED_PARENTHESIS = "ERROR: Parenthesis are not balanced."

EXTRA_SPACES = "ERROR: to many unnecessary spaces."


def unknown_object(token):
    return f' ERROR: "{token}" :unknown object.'


def nonparsable_substring(substring):
    return f' ERROR: "{substring}" can not be parsed.'
