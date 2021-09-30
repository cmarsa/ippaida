# inversepermutation.py

# 1.4.26 Inverse permutation. Compose a program that reads in a
# permutation of the integers 0 to n-1 from n command-line arguments
# and writes its inverse. (If the permutation is an array a[], its
# inverse is the array b[] such that a[b[i]] = b[a[i]] = i.)
# Be sure to check that the input is a valid permutation.
# python inversepermutation.py 4 3 7 2 1 6 5 0
# [4, 3, 7, 2, 1, 6, 5, 0]
# [7, 4, 3, 1, 0, 6, 5, 2]


import sys
import random
import stdio
import stdarray

args_length = len(sys.argv) - 1
a = stdarray.create1D(args_length, 0)
for i in range(0, args_length):
    a[i] = int(sys.argv[i+1])

for i in range(0, len(a)):
    if a[i] < 0 or a[i] >= args_length:
        raise ValueError, 'provide list of integers from 0 to n-1 (n being the number of integer entries)'

b = stdarray.create1D(args_length, 0)
for i in range(0, len(b)):
    b[a[i]] = i

stdio.writeln(a)
stdio.writeln(b)