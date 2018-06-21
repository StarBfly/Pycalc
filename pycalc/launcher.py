#!/usr/bin/env python3.6
import argparse

def _parse_args():
    parser = argparse.ArgumentParser("pycalc")
    parser.add_argument("EXPRESSION", help="expression string to evaluate", type=str)
    parser.add_argument("-m", "--use-modules", metavar="MODULE", nargs="+", help="additional modules to use")
    parser.parse_args()
    return parser.parse_args()


if __name__ == "__main__":
    from calculation import calculate

    args = _parse_args()
    expression = args.EXPRESSION
    result = calculate(expression)
