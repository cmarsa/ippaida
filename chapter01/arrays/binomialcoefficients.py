# binomialcoefficients.py

# 1.4.39 Binomial coefficients. Compose a program that builds and writes a
# two- dimensional ragged array a such that a[n][k] contains the probability
# that you get exactly k heads when you toss a fair coin n times.
# Take a command-line argument to specify the maximum value of n.
# These numbers are known as the binomial distri- bution: if you multiply
# each element in row k by 2 n, you get the binomial coefficients
# (the coefficients of xk in (x+1)n) arranged in Pascals triangle. 
# To compute them, start with a[n][0] = 0.0 for all n and a[1][1] = 1.0,
# then compute values in successive rows, left to right, with a[n][k] = (a[n-1][k] + a[n-1][k-1])/2.0.

import sys
import stdio
import stdarray


n = int(sys.argv[1])

# defining ragged array
binomials = stdarray.create1D(n + 1, [])
for i in range(0, len(binomials)):
    binomials[i] = stdarray.create1D(i + 1, 0.0)

# initializing first binomial coeff
binomials[1][1] = 1.0

# calculating the rest of coefficients
for i in range(2, len(binomials)):
    for k in range(1, len(binomials[i]) - 1):
        binomials[i][k] = (binomials[i-1][k] + binomials[i-1][k-1])/2.0

# printing ragged array
for i in range(1, len(binomials)):
    for j in range(1, len(binomials[i])):
        coefficient = str(binomials[i][j])
        # just giving format to output
        if len(coefficient) < n + 1:
            stdio.write(' '*(n + 1 - len(coefficient)))
        stdio.write(coefficient + ' ')
    stdio.writeln()