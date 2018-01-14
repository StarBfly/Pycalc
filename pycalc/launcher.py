#!/usr/bin/env python3
import sys
from pyparser import parse_expression
from postfix_notation import generate_postfix_notation


def main():
    if len(sys.argv) > 1:
        print(generate_postfix_notation(parse_expression(sys.argv[1])))
    else:
        print("ERROR: no expression given.")


if __name__ == "__main__":
    main()
