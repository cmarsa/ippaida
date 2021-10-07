# randomsurfer.py

# This program uses a transition matrix to simulate the behavior
# of a random surfer. It accepts the number of moves as a
# command-line argument, reads the transition matrix, performs
# the indicated number of moves as prescribed by the matrix, and
# writes the relative frequency of hitting each page. The key
# to the computation is the random move to the next page (see text).

import random
import sys
import stdarray
import stdio

moves = int(sys.argv[1])

n = stdio.readInt()
stdio.readInt()  # | not needed (another n)
                 # | not needed because of the output of the program
                 # | `transition.py`

# reading transition matrix
p = stdarray.create2D(n, n, 0.0)
for i in range(0, n):
    for j in range(0, n):
        p[i][j] = stdio.readFloat()

# random surf
hits = stdarray.create1D(n, 0)
page = 0  # start at page 0
for i in range(0, moves):
    r = random.random()         #  |
    total = 0.0                 #  |  
    for j in range(0, n):       #  |  compute a random page
        total += p[page][j]     #  |  according to distribution
        if r < total:           #  |  in row p[page]
            page = j            #  |
            break               #  |
    hits[page] += 1

#   j           0    1    2    3    4
# p[page][j]   0.47 0.02 0.47 0.02 0.02
# total        0.47 0.49 0.96 0.98 1.0
# Generating a random integer from a discrete distribution


for v in hits:
    stdio.writef('%8.5f', 1.0 * v/moves)
stdio.writeln()
