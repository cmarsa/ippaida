# addints.py

# takes a integer n from the command line and then reads n
# integers from standard input, adds them, and writes the
# sum to standard output.

import sys
import stdio

n = int(sys.argv[1])
total = 0
for i in range(0, n):
    total += stdio.readInt()
stdio.writeln('Sum is ' + str(total))
