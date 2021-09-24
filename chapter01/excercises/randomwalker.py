# randomwalker.py

# 2D random walk. A two-dimensional random walk simulates the behavior
# of a particle moving in a grid of points. At each step, the random walker
# moves north, south, east, or west with probability equal to 1/4,
# independent of previous moves. Compose a program randomwalker.py that takes
# a command-line argu- ment n and estimates how long it will take a
# random walker to hit the boundary of a 2n-by-2n square centered at the starting point.

import sys
import stdio
import random

n = int(sys.argv[1])  # n specifying the dimension of square (2n * 2n)
s = int(sys.argv[2])  # s specifying number of simulations

sum_t = 0
for i in range(0, s):
    x = 0
    y = 0
    t = 0
    while x != n and x != -n and y != n and y != -n:
        t += 1
        sum_t += 1
        step_direction = random.random()
        if step_direction >= 0 and step_direction < 0.25:
            # step to north
            y += 1
        elif step_direction >= 0.25 and step_direction < 0.50:
            # step to east
            x += 1
        if step_direction >= 0.50 and step_direction < 0.75:
            # step to south
            y -= 1
        else:
            # step to west
            x -= 1
    stdio.writeln((i, t))
stdio.writeln('Average time to reach edge: ' + str(sum_t / s))