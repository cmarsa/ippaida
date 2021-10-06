# randomseq.py

# This program accepts an integer command-line argument n,
# and writes to standard output a random sequence of n floats in
# the range [0, 1). The program illustrates the conventional
# model that we have been using so far for Python programming.
# From the program's point of view, there is no limit on the
# length of the output sequence.

import random
import sys
import stdio

n = int(sys.argv[1])
for i in range(0, n):
    stdio.writeln(random.random())
