# shuffletest.py

# 1.4.22 Empirical shuffle check. Run computational experiments to check that
# our shuffling code works as advertised. Compose a
# program shuffletest.py that takes command-line arguments m and n,
# does n shuffles of an array of size m that is initialized
# with a[i] = i before each shuffle, and writes an m-by-m table
# such that row i gives the number of times i wound up in
# position j for all j. All elements in the array should be close to n/m.

import sys
import random
import stdio
import stdarray

m = int(sys.argv[1])
n = int(sys.argv[2])

# initialize array a = [0, 1, ..., n - 1]
a = stdarray.create1D(m, 0)
for i in range(0, m):
    a[i] = i

table = stdarray.create2D(m, m, 0)
# shuffle the deck several times
for j in range(0, n):
    for i in range(0, m):
        a[i] = i
    for i in range(0, len(a)):
        r = random.randrange(0, m)
        temp = a[r]
        a[r] = a[i]
        a[i] = temp
        table[i][r] += 1

# print header of contingency table
stdio.write('    ')
for i in range(0, m):
    if len(str(i)) < 2:
        stdio.write('  ')
    else:
        stdio.write(' ')
    stdio.write(str(i) + ' ')
stdio.writeln()

# print frequencies on m x m basis
i = 0
for row in table:
    if len(str(i)) < 2:
        stdio.write(' ')
    stdio.write(str(i) + ' |')
    for element in row:
        if len(str(element)) < 3:
            stdio.write(' '*(3-len(str(element))))
        stdio.write(str(element) + ' ')
    stdio.writeln()
    i += 1