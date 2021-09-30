# permutationminima.py

# 1.4.25 Minima in permutations. Compose a program that takes an integer
# n from the command line, generates a random permutation, writes the permutation,
# and writes the number of left-to-right minima in the permutation
# (the number of times an element is the smallest seen so far).
# Then compose a program that takes integers m and n from the command line,
# generates m random permutations of size n, and writes the average number of
# left-to-right minima in the permutations generated. Extra credit : Formulate a
# hypothesis about the number of left-to-right minima in a permutation of size n,
# as a function of n.

import sys
import random
import stdio
import stdarray

n = int(sys.argv[1])

# initialize array perm = [0, 1, ..., n - 1]
perm = stdarray.create1D(n, 0)
for i in range(0, n):
    perm[i] = i

# create a random sample of size m in perm[0, ..m)
for i in range(0, n):
    r = random.randrange(i, n)
    # exchange perm[i] and perm[r]
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

minima = perm[0]
minima_count = 1
for i in range(0, len(perm)):
    if perm[i] < minima:
        minima = perm[i]
        minima_count += 1

stdio.writeln(perm)
stdio.writeln('left-to-right minima count: ' + str(minima_count))