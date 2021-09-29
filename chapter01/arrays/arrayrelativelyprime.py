# arrayrelativelyprime.py

# 1.4.14 Compose a program that accepts an integer n from the command
# line and creates an n-by-n boolean array a such that a[i][j] is
# True if i and j are relatively prime (have no common factors)
# and False otherwise. Then write the array (see exercise 1.4.5)
# using * to represent True and a space to represent False. Include row
# and column numbers. Hint: Use sieving.

import sys
import stdio
import stdarray

n = int(sys.argv[1])
n = n+1
M = stdarray.create2D(n, n, False)


for i in range(0, n):
    for j in range(0, n):
        if j != 0 and i != 0:
            # sieve
            a = i
            b = j
            while b != 0:
                a, b = b, a % b
            if a == 1:
                M[i][j] = True

# print array
stdio.write('   ')
for j in range(2, n):
    if len(str(j)) < 2:
        stdio.write(' ')
    stdio.write(str(j) + ' ')
stdio.writeln()
for i in range(2, n):
    if len(str(i)) < 2:
        stdio.write(' ')
    stdio.write(str(i) + '  ')
    for j in range(2, n):
        if M[i][j]:
            stdio.write('*  ')
        else:
            stdio.write('   ')
    stdio.writeln()