# transpose.py

# Compose a code fragment to create a two-dimensional array b[][] that
# is the transpose of an existing m-by-n array a[][].

import random
import sys
import stdarray
import stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

# initialize random matrix of dim(m, n)
M = stdarray.create2D(m, n, 0)
for i in range(0, m):
    for j in range(0, n):
        M[i][j] = random.randint(-10, 10)

# print original matrix
for i in range(0, len(M)):
    for j in range(0, len(M[i])):
        stdio.write(str(M[i][j]) + ' ')
    stdio.writeln()

# create transpose matrix of dim(n, m)
transpose = stdarray.create2D(n, m, 0)
for i in range(0, n):
    for j in range(0, m):
        transpose[i][j] = M[j][i]
stdio.writeln()

# print transpose matrix
for i in range(0, len(transpose)):
    for j in range(0, len(transpose[i])):
        stdio.write(str(transpose[i][j]) + ' ')
    stdio.writeln()
stdio.writeln()
