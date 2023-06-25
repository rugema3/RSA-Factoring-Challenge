#!/usr/bin/env python3

import math
import sys

def factors(num):
    factor = 2
    while factor <= int(math.sqrt(num)):
        if num % factor == 0:
            a = factor
            b = num // factor
            break
        factor = factor + 1
    else:
        a = num
        b = 1
    print("{} = {} * {}".format(num, a, b))

# Check if the filename is provided as an argument
if len(sys.argv) < 2:
    print("Please provide a filename as an argument.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for line in file:
            number = int(line.strip())
            factors(number)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid file content. Please make sure the file contains only numbers.")

