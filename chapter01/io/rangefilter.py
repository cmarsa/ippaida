# rangefilter.py

# This program accepts integer command-line arguments lo and
# hi and then reads integers from standard input until it reaches
# end-of-file, writing to standard output each of those integers
# that is in the range lo to hi, inclusive. Thus the program is a
# filter (see text). There is no limit on the length of the streams.

import sys
import stdio

lo = int(sys.argv[1])
hi = int(sys.argv[2])

while not stdio.isEmpty():
    # process one integer
    value = stdio.readInt()
    if (value >= lo) and (value <= hi):
        stdio.write(str(value) + ' ')
stdio.writeln()
