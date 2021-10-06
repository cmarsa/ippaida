# functiongraph.py

# This program accepts integer command-line argument n and then plots
# a piecewise linear ap- proximation to the function y = sin(4x) + sin(20x)
# by sampling the function at n+1 points between x = 0 and x = pi and drawing
# n line segments. This example illustrates the need for choosing the
# number of samples carefully—on the left, with only 20 samples,
# we miss most of the fluctuations in the curve.

import math
import sys
import stdarray
import stddraw

n = int(sys.argv[1])

x = stdarray.create1D(n + 1, 0.0)
y = stdarray.create1D(n + 1, 0.0)
for i in range(n + 1):
    x[i] = math.pi * i/n
    y[i] = math.sin(4.0 * x[i]) + math.sin(20.0 * x[i])
stddraw.setXscale(0, math.pi)
stddraw.setYscale(-2.0, +2.0)
for i in range(0, n):
    stddraw.line(x[i], y[i], x[i + 1], y[i + 1])
stddraw.show()
