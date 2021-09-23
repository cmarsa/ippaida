# point_in_disk.py

# Compose a program that generates a point that is randomly distributed
# in the unit disk, but without using a break statement.

# I'll use a polar coordinate approach to get the random point,
# then convert to cartesian representation.

import sys
import stdio
import random
import math

PI = 3.1415928

r = random.random()
theta = 2*PI *random.random()

x = r * math.cos(theta)
y = r * math.sin(theta)

stdio.writeln(str(x) + ', ' + str(y))