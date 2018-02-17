from entities import Function


def sqrt(x):
    x = x ** (1.0 / 2)
    return x


def fact(x):
    if x == 1:
        return 1
    else:
        return x * (fact(x - 1))


FUNCTIONS = {
    'abs': Function('abs', abs, 0),
    'max': Function('max', max, 0),
    'sqrt': Function('sqrt', sqrt, 0),
    'fact': Function('fact', fact, 0)
}