# eulerssumofpowersconjecture.py

import sys
import random
import stdio

# Eulers sum-of-powers conjecture. In 1769 Leonhard Euler formulated a
# generalized version of Fermats Last Theorem, conjecturing that at
# least n nth powers are needed to obtain a sum that is itself an nth power,
# for n > 2. Compose a program to disprove Eulers conjecture (which stood until 1967),
# using a quintuply nested loop to find four positive integers whose 5th power sums
# to the 5th power of another positive integer. That is, find five integers a, b, c, d,
# and e such that a^5 + b^5 + c^5 + d^5 = e^5.

# numbers chosen for the ranges in the for loops are chosen for the program
# to converge, as the complexity of the problem is n^5, the combination of numbers
# is very large.

solution_set = set()
for a in range(26, 200):
    for b in range(83, 200):
        for c in range(110, 200):
            for d in range(133, 200):
                for e in range(144, 200):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        if set([a, b, c, d, e]) != solution_set:
                            stdio.writeln('(' + str(a) + ', ' + str(b) + ', ' + str(c) \
                                        + ', ' + str(d) + ', ' + str(e) + ')')
                            solution_set = set([a, b, c, d, e])
                            break