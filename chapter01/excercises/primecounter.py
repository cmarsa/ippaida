# primecounter.py

import sys
import stdio
import time


n = int(sys.argv[1])

tic = time.clock()
for i in range(1, n + 1):
    is_prime = True
    for j in range(1, (i + 1)/2):
        if (j != 1 and j != i) and i % j == 0:
            is_prime = False
    if is_prime:
        stdio.writeln(i)
toc = time.clock()

stdio.writeln('Process time: ' + str(toc - tic) + ' seconds.')