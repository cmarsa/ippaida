# 1_2_21_cont_comp_interest.py
"""
Continuously compounded interest. Compose a program that calculates
and writes the amount of money you would have if you invested it at a given in-
terest rate compounded continuously, taking the number of years t, the principal
P, and the annual interest rate r as command-line arguments. The desired value is
given by the formula Pe^(rt) .
"""

from sys import argv
import math
import stdio

t = int(argv[1])
P = float(argv[2])
r = float(argv[3])

stdio.writeln(
    P * math.exp(r*t)
)