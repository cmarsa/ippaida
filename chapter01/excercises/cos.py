# cos.py

import sys
import stdio

x = float(sys.argv[1])    # x specified in radians
order = int(sys.argv[2])  # approximation order

term = 1
cos_x = 1
sign = -1
for i in range(1, order + 1):
    term *= x / i
    if i % 2 == 0:
        cos_x = cos_x + sign * term
        sign = sign * -1

stdio.writeln(cos_x)
