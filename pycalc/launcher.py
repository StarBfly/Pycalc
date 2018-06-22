#!/usr/bin/env python3.6
import argparse
from pycalc import calculation


def _parse_args():
    parser = argparse.ArgumentParser("pycalc")  # add description
    parser.add_argument("EXPRESSION", help="expression string to evaluate", type=str)
    parser.add_argument("-m", "--use-modules", metavar="MODULE", nargs="+", help="additional modules to use")
    parser.parse_args()
    return parser.parse_args()


def main():
    args = _parse_args()
    expression = args.EXPRESSION
    result = calculation.calculate(expression, args.use_modules)
    print(result)


if __name__ == "__main__":
    main()
