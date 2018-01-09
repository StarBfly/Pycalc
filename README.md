# Pycalc
Pure-python command-line calculator

___

## Requirements
Implement mathematical expression evaluator using python 3.

Calculator should be a command-line utility which receives mathematical
expression string as an argument and prints evaluated result:
```shell
$ pycalc '2+2*2'
6
```

In case of any mistakes in the expression utility should print human-readable error explanation with "ERROR: " prefix:
```shell
$ pycalc '15(25+1'
ERROR: brackets are not balanced
$ calc 'sin(-Pi/4)**1.5'
ERROR: negative number cannot be raised to a fractional power
```

#### Required mathematical operations
* arithmetic (+, -, \*, /, //, %, ^)
* comparison (<, <=, ==, !=, >=, >)
* built-in python functions (abs, pow, round)
* functions from standard python module math (trigonometry, logarithms, etc.)

#### Notes
* Utility should be wrapped into distribution package with setuptools.
* Usage of **eval** and **exec** is prohibited.

---
