# random_between_a_b.py
"""
Compose a program that takes two integers a and b from the command
line and writes a random integer between a and b .
"""
from sys import argv
import random
import stdio

a = int(argv[1])
b = int(argv[2])

c = random.randint(a, b)
stdio.writeln(c)