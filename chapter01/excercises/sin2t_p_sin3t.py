# sin2t_p_sin3t.py
"""
Compose a program that takes a float t from the command line and writes
the value of sin(2t) + sin(3t).
"""
from sys import argv
import math
import stdio


t = float(argv[1])

stdio.writeln(
    math.sin(2*t) + math.sin(3*t)
)