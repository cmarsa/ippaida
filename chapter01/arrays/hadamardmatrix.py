# hadamardmatrix.py

# Hadamard matrix. The n-by-n Hadamard matrix Hn is a boolean matrix
# with the remarkable property that any two rows differ in exactly n/2 elements.
# (This property makes it useful for designing error-correcting codes.)
# H1 is a 1-by-1 ma- trix with the single element True, and for n > 1,
# H2n is obtained by aligning four copies of Hn in a large square,
# and then inverting all of the elements in the lower right n-by-n copy,
# as shown in the following examples (with T representing True and
# F representing False, as usual).

import sys
import stdio
import stdarray
from copy import copy

n = int(sys.argv[1])

assert n % 2 == 0 or n == 1, 'n must be a power of two.'

curr_matrix = stdarray.create2D(1, 1, True)
if n == 1:
    h_matrix = curr_matrix
else:
    power = 1
    while power < n:
        # create hadamard matrix of correct size
        h_matrix = stdarray.create2D(2*power, 2*power, True)
        # get dimension and step size for copying elements
        dim = len(h_matrix)
        square_step = int(round(dim/2.0))
        # copying the previous hadamard matrices into large square
        for i in range(0, dim, square_step):
            for j in range(0, dim, square_step):
                for k in range(0, len(curr_matrix)):
                    for l in range(0, len(curr_matrix)):
                        h_matrix[i + k][j + l] = curr_matrix[k][l]
        # inverting all of the elements in the lower right
        for k in range(0, len(curr_matrix)):
            for l in range(0, len(curr_matrix)):
                h_matrix[square_step + k][square_step + l] = not curr_matrix[k][l]
        # make the hadamard matrix available for next iteration
        curr_matrix = h_matrix
        power *= 2

stdarray.write2D(h_matrix)