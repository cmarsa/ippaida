# both_int_evenly_divide.py
"""
Compose a program that takes two positive integers as command-line ar-
guments and writes T rue if either evenly divides the other.
"""

from sys import argv
import stdio

a = int(argv[1])
b = int(argv[1])

stdio.writeln(
    ((a % b) == 0) or ((b % a) == 0)
)