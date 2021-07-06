# cos_sin_identity.py
"""
Compose a program that uses math.sin() and math.cos() to check that
the value of cos 2  + sin 2  is approximately 1.0 for any  entered as a command-
line argument. Just write the value. Why are the values not always exactly 1.0 ?
"""
from sys import argv
import stdio
import math

theta = float(argv[1])

stdio.writeln(math.cos(theta)**2 + math.sin(theta)**2)