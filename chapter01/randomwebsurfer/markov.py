# markov.py

# This program takes a command-line integer moves,
# reads a transition matrix from standard input, computes
# the probabilities that a random surfer lands on each
# page (page ranks) after moves matrix–vector multiplications,
# and writes the page ranks to standard output.

import sys
import stdarray
import stdio


moves = int(sys.argv[1])
n = stdio.readInt()
stdio.readInt()

# reading transition matrix
p = stdarray.create2D(n, n, 0.0)
for i in range(0, n):
    for j in range(0, n):
        p[i][j] = stdio.readFloat()


ranks = stdarray.create1D(n, 0.0)
ranks[0] = 1.0
for i in range(0, moves):
    new_ranks = stdarray.create1D(n, 0.0)
    for j in range(0, n):
        for k in range(0, n):
            new_ranks[j] += ranks[k] * p[k][j]
    ranks = new_ranks

for i in range(0, n):
    stdio.writef('%8.5f', ranks[i])
stdio.writeln()
