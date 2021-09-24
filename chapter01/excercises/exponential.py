# exponential.py

import sys
import stdio

x = float(sys.argv[1])
order = int(sys.argv[2])

term = 1
exp_x = 0
for i in range(1, order + 1):
    exp_x += term
    term *= x / i
    

stdio.writeln(exp_x)