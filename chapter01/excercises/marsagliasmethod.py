# marsagliasmethod.py

# Compose a program that writes the coordinates of a random
# point (a, b, c) on the surface of a sphere.
# To generate such a point, use Marsaglias method.

import stdio
import random
import math

# get random point from circle
while True:
    x = -1.0 + 2.0 * random.random()
    y = -1.0 + 2.0 * random.random()
    print x, y
    if x*x + y*y <= 1.0:
        break

a = 2 * x * math.sqrt(1 - x**2 - y**2)
b = 2 * math.sqrt(1 - x**2 - y**2)
c = 1 - 2 * (x**2 + y**2)

stdio.writeln('(' + str(a) + ', ' + str(b) + ', ' + str(c) + ')')
