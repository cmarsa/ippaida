# transition.py

# This program is a filter that reads links from standard input
# and writes the corresponding tran- sition matrix to standard output.
# First, it processes the input to count the links from each page.
# Then it applies the 90-10 rule to compute the transition matrix.
# It assumes that there are no pages in the input that have
# zero outdegrees.

import stdarray
import stdio

n = stdio.readInt()

link_counts = stdarray.create2D(n, n, 0)
out_degrees = stdarray.create1D(n, 0)

while not stdio.isEmpty():
    # accumulate link counts
    i = stdio.readInt()
    j = stdio.readInt()
    out_degrees[i] += 1
    link_counts[i][j] += 1

stdio.writeln(str(n) + ' ' + str(n))

for i in range(0, n):
    # write probability distribution for row i
    for j in range(0, n):
        # write probability for column j
        p = (0.90 * link_counts[i][j] / out_degrees[i]) + (0.10 / n)
        stdio.writef('%8.5f', p)
    stdio.writeln()
