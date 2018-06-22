# Python Programming Language Foundation Hometask
You are proposed to implement pure-python command-line calculator
using **python 3.6**.

## Requirements
Calculator should be a command-line utility which receives mathematical
expression string as an argument and prints evaluated result:
```shell
$ pycalc '2+2*2'
6
```

It should provide the following interface:
```shell
$ pycalc --help
usage: pycalc [-h] [-m MODULE [MODULE ...]] EXPRESSION

Pure-python command-line calculator.

positional arguments:
  EXPRESSION            expression string to evaluate

optional arguments:
  -h, --help            show this help message and exit
  -m MODULE [MODULE ...], --use-modules MODULE [MODULE ...]
                        additional modules to use
```

In case of any mistakes in the expression utility should print human-readable
error explanation **with "ERROR: " prefix**:
```shell
$ pycalc '15(25+1'
ERROR: brackets are not balanced
$ pycalc 'sin(-Pi/4)**1.5'
ERROR: negative number cannot be raised to a fractional power
```

### Mathematical operations calculator must support
* arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `^`) (`^` is a power)
* comparison (`<`, `<=`, `==`, `!=`, `>=`, `>`)
* built-in python functions (`abs`, `pow`, `round`)
* functions from standard python module math (trigonometry, logarithms, etc.)
* functions and constants from modules provided with `--use-modules` option


### Non-functional requirements
* It is mandatory to use `argparse` module.
* Codebase must be covered with unittests with at least 70% coverage.
* Usage of **eval** and **exec** is prohibited.

### Distribution
* Utility should be wrapped into distribution package with `setuptools`.
* This package should export CLI utility named `pycalc`.

### Codestyle
* Docstrings are mandatory for all methods, classes, functions and modules.
* Code must correspond to pep8 (use `pycodestyle` utility for self-check).
  * You can set line length up to 120 symbols.

---
Implementations will be checked with the latest cPython interpreter of 3.6 branch.
---