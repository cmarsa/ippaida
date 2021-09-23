# ramanujanstaxi.py

# Ramanujan's taxi. S. Ramanujan was an Indian mathematician who became
# famous for his intuition about numbers. When the English mathematician
# G. H. Hardy came to visit him in the hospital one day,
# Hardy remarked that the num- ber of his taxi was 1729, a rather dull number.
# To which Ramanujan replied, No, Hardy! No, Hardy! It is a very interesting number.
# It is the smallest number express- ible as the sum of two cubes
# in two different ways. Verify this claim by composing a program that
# takes a command-line argument n and writes all integers less than or
# equal to n that can be expressed as the sum of two cubes in two
# different ways. In other words, find distinct positive integers a, b, c,
# and d such that a**3 + b**3 = c**3 + d**3. Use four nested for loops.

import stdio
import sys

n = int(sys.argv[1])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            for d in range(1, n + 1):
                if a**3 + b**3 == c**3 + d**3:
                    if a != c and a != d:
                        if b != a:
                            stdio.writeln(str(a) + '^3 + ' + str(b) + '^3 = ' + str(c) + '^3 + ' + str(d) + '^3')