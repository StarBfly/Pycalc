#!/usr/bin/env python3
import sys
from calculation import calculate


def main():
    if len(sys.argv) > 1:
        print(calculate(sys.argv[1]))
    else:
        print("ERROR: no expression given.")


if __name__ == "__main__":
    main()
