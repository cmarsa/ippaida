# sample.py

# This program accepts integers m and n as command-line arguments,
# and writes a random sample of m integers in the range 0 to n-1
# (no duplicates). This process is useful not just in state and local
# lotteries, but in scientific applications of all sorts. If the first
# argument is less than or equal to the second, the result is a random
# permutation of the integers from 0 to n-1. If the first argument is
# greater than the second, the program raises a ValueError at run time.

import random
import sys
import stdarray
import stdio

m = int(sys.argv[1])   # choose this many elements
n = int(sys.argv[2])   # from 0, 1, ..., n - 1

# initialize array perm = [0, 1, ..., n - 1]
perm = stdarray.create1D(n, 0)
for i in range(0, n):
    perm[i] = i

# create a random sample of size m in perm[0, ..m)
for i in range(0, m):
    r = random.randrange(i, n)
    # exchange perm[i] and perm[r]
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

# write the results
for i in range(0, m):
    stdio.write(str(perm[i]) + ' ')
stdio.writeln()
