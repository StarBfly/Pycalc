#!/usr/bin/env python3
import sys
from parser import parse_expression


def main():
    if len(sys.argv) > 1:
        print(parse_expression(sys.argv[1]))
    else:
        print("ERROR: no expression given.")



if __name__ == "__main__":
    main()