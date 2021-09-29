# transpose.py

# ompose a program that computes the product of two square matrices of
# booleans, using the or operator instead of + and the and operator
# instead of *.

import random
import sys
import stdarray
import stdio


n = int(sys.argv[1])

# initialize random matrices of dim(n, n)
M = stdarray.create2D(n, n, 0)
for i in range(0, n):
    for j in range(0, n):
        M[i][j] = random.randint(0, 1)

N = stdarray.create2D(n, n, 0)
for i in range(0, n):
    for j in range(0, n):
        N[i][j] = random.randint(0, 1)

# print original matrix
stdio.writeln('M: ')
for i in range(0, len(M)):
    for j in range(0, len(M[i])):
        stdio.write(str(M[i][j]) + ' ')
    stdio.writeln()
stdio.writeln()

# print original matrix
stdio.writeln('N: ')
for i in range(0, len(N)):
    for j in range(0, len(N[i])):
        stdio.write(str(N[i][j]) + ' ')
    stdio.writeln()
stdio.writeln()

P = stdarray.create2D(n, n, 0)
for i in range(0, len(M)):
    for j in range(0, len(M[i])):
        for k in range(0, len(N[i])):
            P[i][j] = P[i][j] or M[i][k] and N[k][j]

# print boolean product matrix
stdio.writeln('P = M * N: ')
for i in range(0, len(P)):
    for j in range(0, len(P[i])):
        stdio.write(str(P[i][j]) + ' ')
    stdio.writeln()
stdio.writeln()