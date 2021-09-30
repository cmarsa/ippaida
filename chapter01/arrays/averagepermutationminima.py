# averagepermutationminima.py

# 1.4.25 Minima in permutations. Compose a program that takes an integer
# n from the command line, generates a random permutation, writes the permutation,
# and writes the number of left-to-right minima in the permutation
# (the number of times an element is the smallest seen so far).
# Then compose a program that takes integers m and n from the command line,
# generates m random permutations of size n, and writes the average number of
# left-to-right minima in the permutations generated. Extra credit : Formulate a
# hypothesis about the number of left-to-right minima in a permutation of size n,
# as a function of n.
# Hypothesis: It seems as permutation size grows larger, it also grows
# the average of left-to-right minima count. Growth looks logarithmical.
# python averagepermutationminima.py 1000 5   
# 1.329
# python averagepermutationminima.py 1000 10
# 1.968
# python averagepermutationminima.py 1000 100
# 4.219
# python averagepermutationminima.py 1000 1000
# 6.491
# python averagepermutationminima.py 1000 10000
# 8.832
# python averagepermutationminima.py 1000 100000
# 11.243


import sys
import random
import stdio
import stdarray

m = int(sys.argv[1])   # number of permutations of size n generated
n = int(sys.argv[2])   # permutation size

# initialize array perm = [0, 1, ..., n - 1]
perm = stdarray.create2D(m, n,0)
for i in range(0, m):
    for j in range(0, n):
        perm[i][j] = j

# create a random sample of size m in perm[0, ..m)
minima_count = 1
for i in range(0, m):
    for j in range(0, n):
        r = random.randrange(j, n)
        # exchange perm[i] and perm[r]
        temp = perm[i][r]
        perm[i][r] = perm[i][j]
        perm[i][j] = temp

minima_count = 1
for i in range(0, len(perm)):
    minima = perm[i][0]
    for j in range(0, len(perm[i])):
        if perm[i][j] < minima:
            minima = perm[i][j]
            minima_count += 1

average_minima = minima_count / (m + 0.0)
stdio.writeln(average_minima)