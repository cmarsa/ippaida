# 1_2_20_is_between_march20_and_june20.py
"""
Compose a program that takes two integers m and d from the command
line and writes True if day d of month m is between March 20 and June 20, and
False otherwise. (Interpret m with 1 for January, 2 for February, and so forth.)
"""

from sys import argv
import stdio

m = int(argv[1])
d = int(argv[2])

stdio.writeln(
    (m*d >= 60) and (m*d <= 100)
)