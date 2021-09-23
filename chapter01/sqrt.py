import sys
import stdio

EPSILON = 1e-15

c = float(sys.argv[1])
t = c
while abs(t - c/t) > (EPSILON * t):
    # replace t by the average of t and c/t
    t = (c/t + t) / 2.0
stdio.writeln(t)
