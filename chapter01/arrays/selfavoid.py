# selfavoid.py

# This program accepts integers n and trials as command-line arguments.
# It performs trials experiments, each a random self-avoiding walk
# in an n-by-n lattice, and then writes the percentage of dead ends
# encountered. For each walk, it creates an array of booleans, starts
# the walk in the center, and continues until reaching either a dead
# end or a boundary.

import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])
trials = int(sys.argv[2])
dead_ends = 0
for t in range(trials):
    a = stdarray.create2D(n, n, False)
    x = n // 2
    y = n // 2
    # assure walker is inside delimiting boundary
    while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):
        # check for dead end and make a random move
        a[x][y] = True
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            dead_ends += 1
            break
        r = random.randrange(1, 5)
        if (r == 1) and (not a[x+1][y]):
            x += 1
        elif (r == 2) and (not a[x-1][y]):
            x -= 1
        elif (r == 3) and (not a[x][y+1]):
            y += 1
        elif (r == 4) and (not a[x][y-1]):
            y -= 1
stdio.writeln(str(100*dead_ends // trials) + '% dead ends')
