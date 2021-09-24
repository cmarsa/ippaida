# sin.py

import sys
import stdio

x = float(sys.argv[1])
order = int(sys.argv[2])

term = 1
sin_x = 0
sign = 1
for i in range(1, order + 1):
    term *= x / i
    if i % 2 == 1:
        sin_x = sin_x + sign * term
        sign = sign * -1

stdio.writeln(sin_x)