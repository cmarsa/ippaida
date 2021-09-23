from __future__ import print_function

import sys
import stdio

# to compute the binary representation of n,
# we consider the powers of 2 less than or equal to n
# in decreasing order to determine which belong in the binary
# decompositions (and therefore correspond to a 1 bit in the
# binary representation)

n = int(sys.argv[1])

# compute v as the largest power of 2 <= n
v = 1
while v <= n // 2:
    v *= 2

# cast out powers of 2 in decreasing order
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n-= v
    v //= 2

stdio.writeln()
